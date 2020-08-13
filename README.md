# Шаблон flask приложения с админкой, апи и регистрацией


Создать файл .env из example.env
```
cp example.env .env
```

Инициализация миграций:
```
cd source/
flask db init
```

Импорт миграций:
```
cd source/
flask db upgrate
```

Запуск:
```
cd source/
flask run
```
