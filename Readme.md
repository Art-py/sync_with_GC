# Сервис для синхронизации гугл календаря с БД. 

Для удобства все завернуто в докер контейнеры, которые можно поднять командой из корневого каталога командой: 
```
docker-compose up --build
```

В контейнере pgadmin подключена утилита для доступа к БД, доступен по адресу:
http://127.0.0.1:5050/ - логин/пароль указаны в .env в переменных 
- PGADMIN_DEFAULT_EMAIL
- PGADMIN_DEFAULT_PASSWORD

для подключения к текущей БД, создать новое соединение, назвать можно любым именем.
Данные для подключения так же брать из файла .env из переменных 
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- SQL_HOST
