# Шаблон для выполнения тестового задания

> Привет! `Тут превественная пламенная речь`

----
### Локальный запуск приложения
```shell
docker stop $(docker ps -aq)
docker-compose -f docker-compose.yml -f docker-compose.yml up --build
```

http://localhost:8000/admin/login/?next=/admin/