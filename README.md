# 🚀 SQLGenie: The SQL Chatbot 🧙‍♂️

Welcome to **SQLGenie**, your friendly SQL chatbot designed to assist with database queries and visualization. SQLGenie leverages advanced models like **LLAMA3** and **OpenAI's GPT-3.5-turbo** to answer your SQL queries, generate insightful data visualizations, and provide training plans for your datasets. 


# Demo

<table>
  <tr>
    <td><img src="https://github.com/harshk04/SQLGenie-Final-App/assets/115946158/45c98eb7-d019-430b-a850-2a1743236402" width="500"/></td>
    <td><img src="https://github.com/harshk04/SQLGenie-Final-App/assets/115946158/433beec0-6073-4af0-97a0-8015716e9732" width="500"/></td>
  </tr>

  <tr>
    <td><img src="https://github.com/harshk04/SQLGenie-Final-App/assets/115946158/7b7afdd5-e0c1-4b4b-8a8c-74ae26be3e2b" width="500"/></td>
    <td><img src="https://github.com/harshk04/SQLGenie-Final-App/assets/115946158/f56e0b4f-b25b-41e5-adf2-6ae8d6ee4224" width="500"/></td>
  </tr>
</table>




## 📜 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Models](#models)
- [Database Setup](#database-setup)
- [Training Data](#training-data)
- [Acknowledgements](#acknowledgements)

## 🌟 Features

- **Multi-Model Support**: Switch between LLAMA3 and OpenAI's GPT-3.5-turbo models.
- **Interactive Visualizations**: Generate bar charts, pie charts, histograms, and line charts from your query results.
- **Database Configuration**: Easily switch between different databases (Postgres SQL and MySQL).
- **Training Plan Generation**: Automatically generate and display training plans for your datasets.
- **Session Management**: Retain query results and model states across sessions.

## 🛠 Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/harshk04/sqlgenie.git
    cd sqlgenie
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your database (Postgres SQL example):
    ```sh
    psql -U postgres -f setup.sql
    ```

## 🚀 Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Interact with SQLGenie by entering your SQL queries and selecting the desired visualizations.

## 🔧 Configuration

Configure your database settings in the `app.py` file:

## 🤖 Models

SQLGenie supports two models:

- **LLAMA3**: The default model for generating SQL queries and visualizations.
- **OpenAI GPT-3.5-turbo**: An alternative model that can be selected from the sidebar.

## 🗄 Database Setup

To configure your database, ensure your Postgres or MySQL server is running and accessible. Adjust the database credentials in the `db_configs` section of the `app.py` file.

## 📊 Training Data

SQLGenie uses predefined training data for setting up and querying the database. Check out `training_data.py` for details on the tables and queries used.

## 🙏 Acknowledgements

Special thanks to the developers and contributors of:

- Streamlit
- Plotly
- Pandas
- Qdrant
- OpenAI

Feel free to contribute to this project by opening issues or submitting pull requests. Happy querying with SQLGenie! ✨


## 📬 Contact


If you want to contact me, you can reach me through below handles.

&nbsp;&nbsp;<a href="https://www.linkedin.com/in/harsh-kumawat-069bb324b/"><img src="https://www.felberpr.com/wp-content/uploads/linkedin-logo.png" width="30"></img></a>

