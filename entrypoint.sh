#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Применяем миграции
echo "Running migrations..."
python sync_with_GC/manage.py migrate

# Запускаем сервер разработки
echo "Starting server..."
python sync_with_GC/manage.py runserver 0.0.0.0:8000