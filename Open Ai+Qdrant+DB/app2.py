import streamlit as st
from vanna.openai import OpenAI_Chat
from vanna.qdrant import Qdrant_VectorStore
from qdrant_client import QdrantClient
import pandas as pd

# User inputs for database connection
st.sidebar.header('Database Configuration (Postgres)')
host = st.sidebar.text_input('Host', 'localhost')
dbname = st.sidebar.text_input('Database Name', 'vectordb')
user = st.sidebar.text_input('User', 'postgres')
password = st.sidebar.text_input('Password', 'Harsh@2004', type='password')
port = st.sidebar.text_input('Port', '5432')

# Custom class combining Qdrant_VectorStore and OpenAI_Chat
class MyVanna(Qdrant_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        super().__init__(config)
        self.db_connected = False

    def connect_to_postgres(self, **kwargs):
        try:
            super().connect_to_postgres(**kwargs)
            self.db_connected = True
        except Exception as e:
            st.error(f"Failed to connect to the database: {e}")
            self.db_connected = False

    def run_sql(self, query):
        if not self.db_connected:
            raise Exception("You need to connect to a database first by running vn.connect_to_postgres()")
        return super().run_sql(query)

# Initialize Streamlit app
st.title("Database and Model Training App")

# Configuration
config = {
    'client': QdrantClient(url='http://localhost:6333'),
    'api_key': 'sk-proj-b2IsBrYu00Y7LzhgwwF8T3BlbkFJ0w1PMkqwAshX2NTYS75b',
    'model': 'gpt-3.5-turbo',
}

# Initialize Vanna instance
vn = MyVanna(config=config)

# Automatically connect to the database
with st.spinner('Connecting to database...'):
    vn.connect_to_postgres(host=host, dbname=dbname, user=user, password=password, port=port)

if vn.db_connected:
    st.success('Successfully connected to the database!')
    
    # Step 2: Retrieve and display schema
    try:
        df_information_schema = vn.run_sql("""
            SELECT *
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = 'public' 
        """)
        st.write("Database Schema:")
        st.dataframe(df_information_schema)
        
        # Step 3: Generate and display training plan
        plan = vn.get_training_plan_generic(df_information_schema)
        st.write("Training Plan:")
        st.json(plan.get_summary())
    except Exception as e:
        st.error(f"Failed to retrieve schema or generate training plan: {e}")
else:
    st.error("Failed to connect to the database. Please check your connection details.")

# Step 4: Train the model
if st.button('Train Model'):
    with st.spinner('Training model...'):
        try:
            # Example DDL and training queries
            vn.train(ddl="""
            CREATE TABLE applicants (
                applicantid INT,
                position INT,
                application_date DATE,
                stage VARCHAR(50),
                status VARCHAR(50),
                recruiter VARCHAR(50),
                country VARCHAR(50),
                applicant_name VARCHAR(100),
                salary INT
            );
            """)

            # Adding training queries
            training_data = [
                ("Get the number of applications per country", "SELECT country, COUNT(*) AS number_of_applications FROM applicants GROUP BY country;"),
                ("Find the average salary of applicants who have reached the Test task stage", "SELECT AVG(salary) AS average_salary FROM applicants WHERE stage = 'Test task';"),
                ("List all applicants who have the same name and their application details", "SELECT applicant_name, COUNT(*) AS application_count FROM applicants GROUP BY applicant_name HAVING COUNT(*) > 1;"),
                ("Select all applications that are still open", "SELECT * FROM applicants WHERE status = 'open';"),
                ("Get the total number of applications per recruiter", "SELECT recruiter, COUNT(*) AS number_of_applications FROM applicants GROUP BY recruiter;"),
                ("Find the highest salary expectation among applicants from the United States", "SELECT MAX(salary) AS highest_salary FROM applicants WHERE country = 'United States';"),
                ("Retrieve the list of applicants who applied in October 2018", "SELECT * FROM applicants WHERE application_date BETWEEN '2018-10-01' AND '2018-10-31';"),
                ("Calculate the total number of applications lost at the Profile review stage", "SELECT COUNT(*) AS total_lost_at_profile_review FROM applicants WHERE stage = 'Profile review' AND status = 'lost';"),
                ("Get the average salary for each recruiter", "SELECT recruiter, AVG(salary) AS average_salary FROM applicants GROUP BY recruiter;"),
                ("Find the number of applications per stage", "SELECT stage, COUNT(*) AS number_of_applications FROM applicants GROUP BY stage;"),
                ("Find all matches where the home team won", "SELECT * FROM public.ipl WHERE \"FTR\" = 'H';"),
                ("Calculate the total number of goals scored by each team (both home and away)", 
                    """SELECT "Home" AS Team, SUM("HomeGoals") AS Goals
                       FROM public.ipl
                       GROUP BY "Home"
                       UNION
                       SELECT "Away" AS Team, SUM("AwayGoals") AS Goals
                       FROM public.ipl
                       GROUP BY "Away"
                       ORDER BY Goals DESC;"""),
                ("Find the average number of goals scored in matches for each week",
                    """SELECT "Wk", AVG("HomeGoals" + "AwayGoals") AS AvgGoals
                       FROM public.ipl
                       GROUP BY "Wk";"""),
            ]

            for question, sql in training_data:
                vn.train(question=question, sql=sql)

            st.success('Model training completed!')
        except Exception as e:
            st.error(f"Model training failed: {e}")

# Step 5: Allow user to input queries and display results
st.write("Enter your SQL query:")
user_query = st.text_area("SQL Query", "")

if st.button('Run Query'):
    with st.spinner('Running query...'):
        try:
            if not vn.db_connected:
                vn.connect_to_postgres(host=host, dbname=dbname, user=user, password=password, port=port)

            query_result = vn.ask(user_query)
            st.write("Query Result:")
            st.dataframe(pd.DataFrame(query_result))
        except Exception as e:
            st.error(f"Query failed: {e}")
