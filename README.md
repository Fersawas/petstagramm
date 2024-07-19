# PETSTAGRAMM
## Описание проекта
Проект petstagramm позволяет добавлять информацию о любимых питомцах и редактироватьее.
Реализована регистрация пользователей, добавление, реадктирование, удаление данных о домашних питомцах.  
### Содержанеие

- [Технологии](#tech)
- [Начало работы](#begining)
- [Запуск через docker](#docker)
- [Основные эндпоинты и возможности](#endpoints)

## <a name="tech">Технологии</a>

- [Django](https://www.djangoproject.com/)
- [Django REST](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Djoser](https://djoser.readthedocs.io/en/latest/index.html)

## <a name="begining">Начало работы</a>

### Начало работы

Активируйте вирутальное окржуние:

```
python -m venv venv
```

### Установка зависимостей
Активируйте виртуальное окружение

```
source venv/sqripts/activate
```

Установите зависимости из файла *requirements.txt*:

```
pip install -r requirements.txt
```
Настройте конфигурацию файла .env

### Запуск сервера

Запустите проект:

```
python manage.py runserver
```
## <a name="docker">Запуск через docker</a>
Зайдите в корневую директорию
Запустите dockerfile:

```
docker compose -f docker-compose.yaml up -d
```
## <a name="endpoints">Основные эндпоинты и возможности</a>
Для регистрации пользователя перейдите на ендпоинт
    http://localhost:8000/api/users/users/
Для создания токена
    http://localhost:8000/api/users/jwt/create
Создайте супер пользователя, только он может создавать категории для домашних животных
```
docker compose -f docker-compose.yaml exec backend python mange.py createsuperuser
```
Для фильтрации своих домашних животных и сортировки по категориям используйте 
следующие querry params на эндпоинте http://localhost:8000/api/pets/ ?my_pets=1 покажет 
только ваших домашних питомцев, добавление к нему параметра category=(int:category_id) 
отфильтрует по категориям