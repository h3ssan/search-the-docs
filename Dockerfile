FROM python:3.12-alpine

WORKDIR /app

RUN pip install opensearch-py flask

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8080"]
