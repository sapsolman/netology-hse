# Официальный Python образ в качестве базового
FROM python:3.10-slim

# Устанавливает рабочую директорию
WORKDIR /app

# Устанавливает переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Копирует файл с зависимостями 
COPY requirements.txt /app/

# Устанавливает netcat для проверки доступности базы данных
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Устанавливает зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копирует проект в контейнер
COPY . /app/

# Команда по умолчанию для запуска сервера разработки Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]