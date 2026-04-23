
1. Клонирование репозитория

```bash
# Клонировать репозиторий
git clone https://github.com/sapsolman/netology-hse.git

# Перейти в папку проекта
cd netology-hse
```

2. Сканирование с помощью Локальное сканирование (CLI)

Ввиду текущих проблем версии Python требуемого для запуска проекта и установленной версии локально возникают конфликты принято решение запустить проект Django.Nv в контейнером окружении:

·	Django 1.8.3 — версия указана в requirements.txt и до выхода Python 3.4 или 3.5

·	Python 3.13 (в моей Anaconda) — это свежая версия от 2024 года


3. Запуск через Docker (локально)

**Запуск**

Скачивание и запуск официального образа, монтируем текущую папку $(pwd) внутрь контейнера в /app

*Версия для arm-процессора (Apple Silicone)*

```bash
    docker run --name django-nv-app -p 8000:8000 \
    -v "$(pwd):/app" -w /app \
    python:3.6-slim \
    sh -c "pip install -r requirements.txt && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

```

**Проверка подключения по http://localhost:8000/**

4. Запуск сканирования через Docker

Запуск образа OWASP Zap.

Скачивание и запуск официального образа, монтируем текущую папку $(pwd) внутрь контейнера в /app

*Версия для arm-процессора (Apple Silicone)*

```bash
    docker run --rm -u root -v "$(pwd):/zap/wrk/:rw" \
    -t zaproxy/zap-stable zap-baseline.py \
    -t http://host.docker.internal:8000 \
    -J zap-report.json -x zap-report.xml

```

5. Конфигурация в GitLab

**Запуск**

Используется файл-пайплайна:

[.gitlab-ci.yml](.gitlab-ci.yml)

**VMS**

Используется файл-пайплайна + конфиг для выгрузки в Dojo:

[.gitlab-ci-dojo.yml](.gitlab-ci-dojo.yml)

[dojo_upload.py](dojo_upload.py)