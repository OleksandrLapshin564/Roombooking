FROM python:3.9-slim

# Installing the required packages for psycopg2 and netcat (for wait-for-it.sh)
RUN apt-get update \
    && apt-get install -y libpq-dev gcc netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# If Pillow is not in requirements.txt, install it here (or add it to requirements.txt)
# RUN pip install Pillow

# Copy the rest of the application code
COPY . /app/

# Copy the wait-for-it script and grant it execution rights.
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

EXPOSE 8000

# Server startup command (uses wait-for-it.sh to wait for the database)
CMD ["bash", "wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
