from vanna.ollama import Ollama
from vanna.qdrant import Qdrant_VectorStore
from qdrant_client import QdrantClient
import pandas as pd
import plotly.express as px
import training_data

class MyVanna(Qdrant_VectorStore, Ollama):
    def __init__(self, config=None):
        Qdrant_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

    def connect_and_setup(self):
        self.connect_to_postgres(host='localhost', dbname='university', user='postgres', password='Harsh@2004', port='5432')

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

        for doc in training_data.documentation:
            self.train(documentation=doc)


        # for question, sql in training_data.queries_applicants:
        #     self.train(question=question, sql=sql)

        # self.train(documentation=training_data.documentation2)

    def get_training_data_info(self):
        return self.get_training_data()

    def ask_question(self, question):
        result = self.ask(question)
        if isinstance(result, tuple) and len(result) == 3:
            query, dataframe, figure = result
            if isinstance(dataframe, pd.DataFrame) and isinstance(figure, dict):
                fig = px.bar(dataframe, x='applicant_name', y='salary', title='-')
                return query, dataframe, fig
        return result

# Initialization
config = {'client': QdrantClient(url='http://localhost:6333'), 'model': 'llama3'}
vn = MyVanna(config=config)

# Connect and setup
df_information_schema = vn.connect_and_setup()

# Generate plan and train
plan = vn.generate_plan_and_train(df_information_schema)

# Create table and inspect training data
vn.create_table()
training_data = vn.get_training_data_info()

# This function can be called from the Streamlit app
def query_vanna(question):
    return vn.ask_question(question)

def show_training_data():
    return training_data
