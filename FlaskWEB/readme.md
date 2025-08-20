# Настройка окружения

```commandline
pip install flask flask-sqlalchemy flask-migrate
```


# Миграции
```commandline
flask db init
```

```commandline
flask db migrate -m "Initial migration"
```

```commandline
 flask db upgrade
```

```commandline
 flask db migrate -m "Комментарий"
```

# Запуск приложения

```cmd
python app.py 
```