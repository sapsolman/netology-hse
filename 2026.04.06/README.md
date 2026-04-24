

1. Клонирование репозитория

```bash
    # Клонировать репозиторий
    git clone https://github.com/sapsolman/netology-hse.git

    # Перейти в папку проекта
    cd netology-hse
```

2. Установка Trivy и Bandit (macOS версии)

```bash
    # Установить Trivy
    brew install trivy

    # Установить Bandit
    brew install bandit
```

3. Сканирование с помощью Локальное сканирование (CLI)

**Запуск Trivy**

```bash
    trivy fs . --format json --output trivy-report.json

    # fs - указание на файловую систему
    # . - путь к репо
    # --format - задает формат
    # --output - вывод в файл
```

**Запуск Bandit**

```bash
    bandit -r . -f json -o bandit-report.json
    # -r - рекурсивный обход всех вложенных папок
    # -f задает формат
    # -o - вывод в файл
```

4. Сканирование через Docker

**Запуск Trivy**

Скачивание и запуск официального образа, монтируем текущую папку $(pwd) внутрь контейнера в /app

*Версия для arm-процессора (Apple Silicone)*
```bash
    docker run --rm -v "$(pwd):/app" \
    aquasec/trivy:0.69.3-arm64 fs /app \
    --format json \
    --output /app/trivy-docker-report.json
```

**Запуск Bandit**

Скачивание и запуск официального образа, монтируем текущую папку $(pwd) внутрь контейнера в /app

*Версия для arm-процессора (Apple Silicone)*

```bash
    docker run --rm -v "$(pwd):/app" \
    aquasec/trivy:0.69.3-arm64 fs /app \
    --format json \
    --output /app/trivy-docker-report.json
```

4. Конфигурация в GitLab

Используется файл-пайплайна

[.gitlab-ci.yml](.gitlab-ci.yml)
