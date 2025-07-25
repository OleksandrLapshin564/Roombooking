# Using the base Python image
FROM python:3.9-slim

# Installing the necessary libraries for psycopg2
RUN apt-get update \
    && apt-get install -y libpq-dev gcc netcat-openbsd

# Creating a working directory
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Project launch command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
