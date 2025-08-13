FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y libpq-dev gcc netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

EXPOSE 8001

CMD ["bash", "wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8001"]
