# Wildberries Analytics Platform 
Этот проект представляет собой аналитическую платформу для товаров Wildberries, позволяющую парсить данные о товарах, анализировать их и визуализировать результаты.

## Структура проекта
```plaintext
/my_project
.
├── db.sqlite3                     # База данных SQLite
├── manage.py                      # Скрипт управления Django
├── myapp                          # Основное приложение
│   ├── admin.py                   # Настройки админ-панели
│   ├── apps.py                    # Конфигурация приложения
│   ├── filters.py                 # Фильтры для API
│   ├── management
│   │   └── commands
│   │       ├── parse_wildberries.py # Команда для парсинга
│   ├── migrations                 # Миграции базы данных
│   ├── models.py                  # Модели данных
│   ├── serializers.py             # Сериализаторы для API
│   ├── task.py                    # Логика парсинга
│   ├── templates                  # HTML шаблоны
│   │   ├── index.html             # Главная страница
│   │   └── product_list.html      # Страница списка товаров
│   ├── urls.py                    # URL-адреса приложения
│   └── views.py                   # Контроллеры
├── myproject                      # Конфигурация проекта
│   ├── settings.py                # Настройки проекта
│   └── urls.py                    # Корневые URL-адреса
├── requirements.txt               # Зависимости
└── static                         # Статические файлы
    ├── css
    │   └── style.css              # Стили
    └── js
        └── script.js              # JavaScript
```

## Основные возможности
### 1.Парсинг данных с Wildberries

-Поиск товаров по запросу пользователя

-Сохранение данных в базу:

-Название товара

-Цена и цена со скидкой

-Рейтинг

-Количество отзывов

-Ссылка на товар

### 2.Аналитическая панель

1.Таблица товаров с фильтрацией и сортировкой

2.Динамические графики:

-Гистограмма распределения цен

-График зависимости скидки от рейтинга

### 3.API

-Эндпоинт /api/products/ для получения данных

-Поддержка фильтрации по цене, рейтингу и количеству отзывов

## Запуск проекта

### Требования
Python 3.10+

Установленные зависимости из requirements.txt

## Установка
Клонируйте репозиторий:

 ```bash
git clone https://github.com/podlizka-2/my_project.git
cd /my_project
 ```
Создайте виртуальное окружение:
 ```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
 ```
Установите зависимости:

 ```bash
pip install -r requirements.txt
 ```
Примените миграции:

 ```bash
python manage.py migrate
 ```
Запуск
 ```bash
python manage.py runserver
 ```
После запуска откройте в браузере: http://127.0.0.1:8000/