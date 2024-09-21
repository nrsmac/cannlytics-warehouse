# Use Python 3.9 as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY src/frontend/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Copy the current directory contents into the container at /app
COPY ./src/frontend/* /app
COPY duckdb.db /app/

# Define environment variables
ENV STREAMLIT_SERVER_ADDRESS="0.0.0.0"

# Run the Streamlit app
CMD ["streamlit", "run", "Home.py"]