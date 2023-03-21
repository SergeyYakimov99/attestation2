Post
О проекте
Программа разработки собственного API сервиса для создания постов. В проекте используется: Python, Django

В приложении реализованы следующие функции:

Созданы основные модели для БД. 
Создан суперпользователя с логином и паролем admin и заполнена таблица тестовыми данными. 

Установка зависимостей:

В корневой папке находиться файл с зависимостями requirements.txt

pip install -r requirements.txt

Stack
Python 3.10, Django 4.0.1, Postgres

Запуск приложения:
Установить зависимости
Заполнить .env со значениями, в котором следует хранить настройки по умолчанию;
Накатить миграции.
python ./manage.py migrate
Запустить проект.