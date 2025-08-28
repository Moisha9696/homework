# Устновка Django

```commandline
 pip install djangorestframework
```
# Создание сурер-пользователя
```commandline
python manage.py createsuperuser
```

## Добавление JWT
```commandline
djangorestframework-simplejwt
```

### Изменения в Djano 
```pithon
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'rest_framework',
    'rest_framework_simplejwt',
```

# Работа с миграциями

## Создание
```commandline
python manage.py makemigrations
```

## Миграция
```commandline
python manage.py migrate 
```

# Запуск сервера
```commandline
 python manage.py runserver
```