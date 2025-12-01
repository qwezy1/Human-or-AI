FROM python:3.13-slim

WORKDIR /app

COPY app/ ./app
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "app/main.py"]
