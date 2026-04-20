#!/bin/sh

# Stop on error
set -e

echo "Применение миграций базы данных..."
python manage.py migrate --noinput

echo "Сборка статических файлов..."
python manage.py collectstatic --noinput || true

# Выполняем команду, переданную в CMD (runserver или gunicorn)
exec "$@"