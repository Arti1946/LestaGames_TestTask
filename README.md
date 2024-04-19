# Test Task for Lesta Games Company


## Установка

* Клонировать репозиторий командой `git clone`
* Создать виртуальное окружение командой `python -m venv venv` и активировать его командой `source venv/Scripts/activate`
* Установить зависимости командой `pip install -r requirements.txt`
* Перейти в директорию с файлом _**manage.py**_ 
* Подготовить миграции командой `python manage.py makemigrations` и запустить их `python manage.py migrate`
* Запустить приложение командой `python manage.py runserver`

## Доступные эндпоинты
* Загрузка файла - [http://127.0.0.1:8000/upload_file/](http://127.0.0.1:8000/upload_file/)
* Отображение таблицы со списком слов из файла и их idf, tf - http://127.0.0.1:8000/table/<название файла>/