**1. Сборка Docker-образа** \
Находясь в корневой папке проекта (где расположен Dockerfile), выполните команду сборки образа и присвойте ему тег django-app:

```bash
    docker build -t django-simple-app:v1 . 
```

**2. Запуск приложения в контейнере** \
Запустите собранный контейнер в фоновом режиме (-d). Мы пробрасываем порт 80 вашей локальной машины на порт 8000 внутри контейнера (где запущен Django):

```bash
    docker run -d -p 80:8000 --name django-simple-container django-simple-app:v1
```

**3. Проверка результата** \
Убедиться в запуске контейнера

```bash
    docker ps
```

Откройте браузер и перейдите по адресу:
http://localhost:80 (или http://localhost).

В результате выполнения будет отображена страница с ракетой и текст:
***
*The install worked successfully! Congratulations!
You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.*
***

![It works](staff/django_simple.png)

***Дополнительная информация:*** \
Содержимое директории jproject и файла manage.py были получены путём запуска команды:

    ```bash
    docker run --rm -v $(pwd):/app \
    -w /app python:3.10-slim sh \
    -c "pip install -r requirements.txt && django-admin startproject jproject ."
```

Структура проекта:
```Plaintext
django-demo/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    ├── manage.py
    ├── nginx/
        └── default.conf
    └── jproject/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    staff/
        ├── django_simple.png
        ├── django_trio.png
    README.md
```

**4. Опционально:** \
Запуск приложения с использованием docker compose. \
Используется связка PostgreSQL + Django + Nginx.

```bash
    docker compose up -d --build
```

В результате запуска получаем связку из 3х компонентов

![It works](staff/django_trio.png)