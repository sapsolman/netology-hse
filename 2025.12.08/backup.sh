#!/bin/bash
# Скрипт резервного копирования

# Проверяем количество аргументов
if [ $# -ne 2 ]; then
    echo "Использование: $0 <исходная_директория> <целевая_директория>"
    exit 1
fi

# Сохраняем аргументы
source_dir="$1"
target_dir="$2"

# Получаем текущую дату в формате ГГГГ-ММ-ДД
current_date=$(date +%Y-%m-%d)

# Проверяем существование исходной директории
if [ ! -d "$source_dir" ]; then
    echo "Исходная директория $source_dir не существует!"
    exit 1
fi

# Создаем целевую директорию, если её нет
mkdir -p "$target_dir"

echo "Начинаем резервное копирование..."
echo "Из: $source_dir"
echo "В: $target_dir"

# Копируем каждый файл из исходной директории
# find ищет файлы в директории
# -type f - только файлы (не директории)
find "$source_dir" -type f | while read -r file; do
    # Получаем только имя файла (без пути)
    filename=$(basename "$file")
    # Создаем новое имя с датой
    new_filename="${filename%.*}_${current_date}.${filename##*.}"
    # Копируем файл с новым именем
    cp "$file" "$target_dir/$new_filename"
    echo "Скопирован: $filename -> $new_filename"
done

echo "Резервное копирование завершено!"