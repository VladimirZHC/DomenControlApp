# DomenControlApp
imitating domen control

# domencontrol 
## Установка  
Склонируйте репозиторий.  
В папке **domencontrol** создайте файл `.env` с ключом `SECRET_KEY='<your_key>'`, это необходимо для работы Django. Можете придумать свой ключ, или воспользоваться генератором (например [djecrety](https://djecrety.ir/)).  
*До конца установки все команды выполняются из корневой директории проекта.*  
Установите виртуальное окружение: `python -m venv venv`  
Активируйте его:
- на linux/mac: `source venv/bin/activate`  
- на windows: `source venv\Scripts\activate`

Установите зависимости:  
`pip install -r requirements.txt`  
Проведите миграции БД:  
`python manage.py migrate`  
Создайте суперпользователя:  
`python manage.py createsuperuser`  
Запустите сервер разработчика:  
`python manage.py runserver`  
Приложение доступно по адресу [localhost:8000](http://localhost:8000/)  
## Использование  
Взаимодействие происходит через ресурс (http://localhost:8000)  
Подробная документация по ресурсам доступна по адресу [/openapi](http://localhost:8000/api/v1/openapi/)  
В приложении работает стандартная административная панель Django - [localhost:8000/admin](http://localhost:8000/admin/)  

