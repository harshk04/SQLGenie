import streamlit as st
import importlib
import pandas as pd
import plotly.express as px
import time

# Database configuration
db_configs = {
    "Postgres SQL": {
        "host": "localhost",
        "dbname": "university",
        "user": "postgres",
        "password": "Harsh@2004",
        "port": 5432
    },
    # "MySQL": {
    #     "host": "localhost",
    #     "dbname": "mydb",
    #     "user": "root",
    #     "password": "password",
    #     "port": 3306
    # }
}

# Initialize session state for model if not already sets
if 'model' not in st.session_state:
    st.session_state.model = 'llama3'

# Function to reload the module based on model choice
def reload_module(model_name):
    if model_name == 'llama3':
        return importlib.import_module('llama3')
    elif model_name == 'openai':
        return importlib.import_module('model')
    elif model_name == 'sqlcoder':
        return importlib.import_module('sqlcoder')
        
current_module = reload_module(st.session_state.model)

# Sidebar for database selection
st.sidebar.title("Database Settings")
db_choice = st.sidebar.selectbox("Select Database", ("Postgres SQL", "MySQL"))

# Sidebar for model selection
model_choice = st.sidebar.selectbox("Change Model", ("LLAMA3", "OpenAI", "SQLCoder"))
if st.sidebar.button("Apply Model Change"):
    if model_choice.lower() != st.session_state.model:
        st.session_state.model = model_choice.lower()
        current_module = reload_module(st.session_state.model)
        st.sidebar.write(f"Model changed to {model_choice}")

with st.sidebar.expander("Database Configuration"):
    if db_choice == "MySQL":
        st.write("Not configured yet.")
    else:
        db_config = db_configs[db_choice]
        st.write(f"Host: {db_config['host']}")
        st.write(f"Database Name: {db_config['dbname']}")
        st.write(f"User: {db_config['user']}")
        st.write(f"Password: {db_config['password']}")
        st.write(f"Port: {db_config['port']}")

# Main Interfaces
st.title("SQLGenie: The SQL Chatbot")
st.warning(f"Currently selected model: {st.session_state.model.upper()}")

# Function to format and display the result
def display_result(result):
    if isinstance(result, pd.DataFrame):
        st.dataframe(result)
    elif isinstance(result, tuple):
        query, dataframe, _ = result
        st.write("Query:")
        st.success(f"{query}")
        
        if isinstance(dataframe, pd.DataFrame):
            st.dataframe(dataframe)
            
            # Chart type selection with a unique key
            chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Pie Chart", "Histogram", "Line Chart"], index=0, key="chart_type")
            
            # Extract columns from the dataframe
            columns = dataframe.columns.tolist()
            
            # Allow the user to select x and y axes for the chart with unique keys
            x_axis = st.selectbox("Select X Axis", columns, key="x_axis")
            y_axis = st.selectbox("Select Y Axis", columns, key="y_axis")
            
            # Generate and display the selected chart
            if chart_type == "Bar Chart":
                fig = px.bar(dataframe, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
            elif chart_type == "Pie Chart":
                fig = px.pie(dataframe, names=x_axis, values=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
            elif chart_type == "Histogram":
                fig = px.histogram(dataframe, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
            elif chart_type == "Line Chart":
                fig = px.line(dataframe, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
            
            st.plotly_chart(fig)
        else:
            st.write("No valid data returned to display chart.")
    else:
        st.write(result)

# Input and buttons
question = st.text_input("Enter your question:", "")
if st.button("Submit"):
    if question:
        with st.spinner("Generating Response..."):
            answer = current_module.query_vanna(question)
        st.session_state['answer'] = answer
        display_result(answer)
    else:
        st.error("Please enter a question to proceed.")

if st.button("Show Training Data"):
    with st.spinner("Fetching Training Data..."):
        time.sleep(1)
        training_data = current_module.show_training_data()
    st.dataframe(training_data)

# Display the training plan summary
with st.spinner("Generating Training Plan..."):
    time.sleep(1)
    df_information_schema = current_module.vn.connect_and_setup()
    plan = current_module.vn.get_training_plan_generic(df_information_schema)
st.write("Training Plan:")
st.json(plan.get_summary())

# Display the stored result
if 'answer' in st.session_state:
    display_result(st.session_state['answer'])
