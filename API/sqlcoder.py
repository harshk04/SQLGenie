from vanna.ollama import Ollama
from vanna.qdrant import Qdrant_VectorStore
from qdrant_client import QdrantClient
import pandas as pd
import plotly.express as px
import training_data

class SQLCoder(Qdrant_VectorStore, Ollama):
    def __init__(self, config=None):
        Qdrant_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

    def connect_and_setup(self, host, dbname, user, password, port):
        self.connect_to_postgres(host=host, dbname=dbname, user=user, password=password, port=port)

        df_information_schema = self.run_sql("""
            SELECT *
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = 'public'
        """)
        return df_information_schema

    def generate_plan_and_train(self, df_information_schema):
        plan = self.get_training_plan_generic(df_information_schema)
        self.train(plan=plan)
        return plan

    def create_table(self):
        self.train(ddl=training_data.ddl_departments)
        self.train(ddl=training_data.ddl_students)
        self.train(ddl=training_data.ddl_courses)
        self.train(ddl=training_data.ddl_enrollments)
        self.train(ddl=training_data.ddl_professors)

        for question, sql in training_data.queries:
            self.train(question=question, sql=sql)

    def get_training_data_info(self):
        return self.get_training_data()

    def ask_question(self, question):
        result = self.ask(question)
        if isinstance(result, tuple) and len(result) == 3:
            query, dataframe, figure = result
            if isinstance(dataframe, pd.DataFrame):
                dataframe_dict = dataframe.to_dict(orient='records')
                if isinstance(figure, dict):
                    fig = px.bar(dataframe, x='applicant_name', y='salary', title='-')
                    return {
                        'query': query,
                        'dataframe': dataframe_dict,
                        'figure': fig.to_json()
                    }
        return result

def run_query(connection_details, query):
    config = {'client': QdrantClient(url='http://localhost:6333'), 'model': 'sqlcoder'}
    vn = SQLCoder(config=config)

    # Connect and setup
    vn.connect_and_setup(
        host=connection_details['host'],
        dbname=connection_details['dbname'],
        user=connection_details['user'],
        password=connection_details['password'],
        port=connection_details['port']
    )

    # Execute the query
    return vn.ask_question(query)
