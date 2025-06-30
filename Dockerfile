# Используем официальный образ Python
FROM python:3.9-slim

# Создаем и переходим в рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY myapp/ ./myapp/
COPY myproject/ ./myproject/
COPY static/ ./static/
COPY manage.py .

# Собираем статику
#RUN python manage.py collectstatic --noinput

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]