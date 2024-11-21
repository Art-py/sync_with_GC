FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
COPY entrypoint.sh /app/

RUN apt-get update && apt-get install -y netcat-openbsd libpq-dev gcc

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]