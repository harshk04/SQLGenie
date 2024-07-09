# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install build tools
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Set the Streamlit configuration environment variables
ENV STREAMLIT_SERVER_HEADLESS=true

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
