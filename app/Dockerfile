FROM python:3.13-slim

WORKDIR /app

# копируем код приложения
COPY app/ ./app

# копируем requirements.txt из корня проекта
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000
CMD ["python", "main.py"]
