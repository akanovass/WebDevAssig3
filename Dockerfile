# Используем образ Python 3.9
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Открываем порт 8000 для доступа к приложению Django
EXPOSE 8000

# Команда для запуска сервера Django при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
 
