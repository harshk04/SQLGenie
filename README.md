# 🚀 SQLGenie: The SQL Chatbot 🧙‍♂️

Welcome to **SQLGenie**, your friendly SQL chatbot designed to assist with database queries and visualization. SQLGenie leverages advanced models like **LLAMA3** and **OpenAI's GPT-3.5-turbo** to answer your SQL queries, generate insightful data visualizations, and provide training plans for your datasets. Additionally, SQLGenie is integrated with the **SQLCoder LLM provided by Defog AI** for enhanced query capabilities.


## Demo

| ![Screenshot 2024-07-12 at 3 10 16 PM](https://github.com/user-attachments/assets/16c1407e-1963-4b41-ac8e-f2ef8fe0dd1f) | ![Screenshot 2024-07-12 at 3 10 44 PM](https://github.com/user-attachments/assets/51ed02e1-65b4-4605-ab0a-2963cfce609b) |
|:--:|:--:|
| **Image 1** | **Image 2** |
| ![Screenshot 2024-07-12 at 3 23 07 PM](https://github.com/user-attachments/assets/bc3b3818-5f28-4edd-9679-10230bf3a57f) | ![Screenshot 2024-07-12 at 3 23 22 PM](https://github.com/user-attachments/assets/657b32ff-1896-44fa-b660-080440f62e11) |
| **Image 3** | **Image 4** |



## 📜 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Models](#models)
- [Database Setup](#database-setup)
- [Training Data](#training-data)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## 🌟 Features

- **Multi-Model Support**: Switch between LLAMA3 and OpenAI's GPT-3.5-turbo models.
- **Interactive Visualizations**: Generate bar charts, pie charts, histograms, and line charts from your query results.
- **Database Configuration**: Easily switch between different databases (Postgres SQL and MySQL).
- **Training Plan Generation**: Automatically generate and display training plans for your datasets.
- **Session Management**: Retain query results and model states across sessions.
- **SQLCoder LLM Integration**: Utilize the SQLCoder LLM by Defog AI for enhanced SQL query generation.

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

4. Build and run the Docker container:
    ```sh
    docker build -t sqlgenie .
    docker run -p 5000:5000 sqlgenie
    ```

## 🚀 Usage

1. **Create and run Qdrant Docker image:**
    ```sh
    docker run -p 6333:6333 -p 6334:6334 \
        -v $(pwd)/qdrant_storage:/qdrant/storage:z \
        qdrant/qdrant
    ```

2. **Install and run Ollama on your local machine:**
    - Follow the [Ollama installation guide](https://docs.ollama.ai/installation) for your operating system.
    - Start Ollama service:
        ```sh
        ollama start
        ```

3. **Run the Flask app:**
    ```sh
    python main.py
    ```

4. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

5. Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

6. Interact with SQLGenie by entering your SQL queries and selecting the desired visualizations.

## 🔧 Configuration

Configure your database settings in the `app.py` file.

## 🤖 Models

SQLGenie supports three models:
- **LLAMA3**: The default model for generating SQL queries and visualizations.
- **OpenAI GPT-3.5-turbo**: An alternative model that can be selected from the sidebar.
- **SQLCoder LLM by Defog AI**: Integrated for enhanced SQL query generation.

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
- Defog AI

Feel free to contribute to this project by opening issues or submitting pull requests. Happy querying with SQLGenie! ✨

## 📬 Contact

If you want to contact me, you can reach me through the below handle.

&nbsp;&nbsp;<a href="https://www.linkedin.com/in/harsh-kumawat-069bb324b/"><img src="https://www.felberpr.com/wp-content/uploads/linkedin-logo.png" width="30"></img></a>
