# -----------------------------
# Base Python image
# -----------------------------
FROM python:3.9-slim

# -----------------------------
# Install necessary system libraries for psycopg2 and netcat
# -----------------------------
RUN apt-get update \
    && apt-get install -y libpq-dev gcc netcat-traditional \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



# -----------------------------
# Set working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Copy and install Python dependencies
# -----------------------------
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy project files
# -----------------------------
COPY . /app/

# -----------------------------
# Ensure wait-for-it.sh is executable
# -----------------------------
RUN chmod +x /app/wait-for-it.sh

# -----------------------------
# Expose port to match docker-compose
# -----------------------------
EXPOSE 8001

# -----------------------------
# Default command to launch the project
# -----------------------------
CMD ["sh", "-c", "./wait-for-it.sh db:5432 -- python manage.py runserver 0.0.0.0:8001"]
