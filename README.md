# ITFactory
версия python 3.6+
1) клонирование проекта
2) создание файла .env на уровне с директорией core по примеру .env.example
3) запуск проекта в докере командой sudo docker-compose up --build
4) создать админа 
    4.1) прописать команду sudo docker ps и скопировать id контейнера web_itfactory
    4.2) создать пользователя командой sudo docker exec -it CONTAINER_ID python manage.py createsuperuser
5) перейти по адресу http://0.0.0.0:8000/api/swagger
6) все существующие url увидите в документации swagger
