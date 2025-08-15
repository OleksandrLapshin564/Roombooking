# --- Base image ---
FROM python:3.9-slim

# --- Install system dependencies ---
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libpq-dev \
       gcc \
       netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# --- Set work directory ---
WORKDIR /app

# --- Install Python dependencies ---
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# --- Copy all project files (including wait-for-it.sh) ---
COPY . /app/

# --- Make wait-for-it.sh executable ---
RUN chmod +x /app/wait-for-it.sh

# --- Expose Django port ---
EXPOSE 8001

# --- Default command ---
CMD ["bash", "/app/wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8001"]
