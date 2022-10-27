# Дипломный проект «Foodgram»
## Описание
Foodgram, «Продуктовый помощник». Онлайн-сервис и API для него. На этом сервисе 
пользователи могут публиковать рецепты, подписываться на публикации других 
пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед 
походом в магазин скачивать сводный список продуктов, необходимых 
для приготовления одного или нескольких выбранных блюд.

Проект доступен по адресу [gregfedy.sytes.net](http://gregfedy.sytes.net/)<br>
Документация к API доступна по адресу [gregfedy.sytes.net/api/docs/](http://gregfedy.sytes.net/api/docs/)<br>
Админ-зона доступна по адресу [gregfedy.sytes.net/admin/](http://gregfedy.sytes.net/admin/)<br>

### Функционал API:
#### AUTH
- Получение **JWT-токена** в обмен на **password** и **email**
- Удаление **JWT-токена** текущего пользователя
#### USERS
- Регистрация пользователя
- Изменение пароля текущего пользователя
- Получение списка пользователей
- Получение профиля пользователя по id
- Получение профиля текущего пользователя
#### TAGS
- Получение списка всех тегов
- Получение тега по id
#### RECIPES
- Получение списка всех рецептов
- Создание рецепта
- Получение рецепта по id
- Изменение рецепта по id
- Удаление рецепта по id
#### SHOPPING_CART
- Скачивание файла со списком покупок
- Добавление рецепта в список покупок по id
- Удаление рецепта из списка покупок по id
#### FAVORITES
- Добавление рецепта в избранное по id
- Удаление рецепта из избранного по id
#### FOLLOWS
- Получение списка подписок текущего пользователя
- Подписка на пользователя по id
- Отписка от пользователя по id
#### INGREDIENTS
- Получение списка всех ингредиентов
- Получение ингредиента по id

#### Для регистрации новых пользователей:
1. Необходимо отправить POST-запрос на добавление нового пользователя
с параметрами **email**, **username**, **first_name**, **last_name**,
**password** на эндпоинт `/api/users/`.
2. Дальше необходимо отправить POST-запрос с параметрами **password**
и **email** на эндпоинт `/api/auth/token/login/`, в ответе на запрос
придёт token (JWT-токен).
3. При желании можно отправить POST-запрос на эндпоинт `/api/auth/token/logout/`
для удаления JWT-токена.

## Установка
### Шаг 1. Установка Docker
Cкачать [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux следует убедиться, что установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Официальная [инструкция](https://docs.docker.com/engine/install/) по установке Docker.

### Шаг 2. Создать файл .env в директории /infra внутри приложения
Пример:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=...
DEBUG=False
ALLOWED_HOSTS=127.0.0.1
```

### Шаг 3. Запуск docker-compose
Для запуска необходимо выполнить из директории /infra команду:
```bash
docker-compose up -d
```

### Шаг 4. Создание базы данных
Применяем миграции:
```bash
docker-compose exec backend python manage.py migrate
```
### Шаг 5. Создание суперпользователя
Создание суперпользователя:
```bash
docker-compose exec backend python manage.py createsuperuser
```

### Шаг 6. Подгружаем статику
Выполните команду:
```bash
docker-compose exec backend python manage.py collectstatic --no-input 
```

### Шаг 7. Заполнение базы тестовыми данными
Для заполнения базы тестовыми данными вы можете использовать файл
ingredients.csv, который находится в директории /data. Выполните команду:
```bash
docker-compose exec backend python manage.py load_csv data/
```

### Другие команды
Остановить работу всех контейнеров можно командой:
```bash
docker-compose down
```

Для пересборки и запуска контейнеров воспользуйтесь командой:
```bash
docker-compose up -d --build 
```

Мониторинг запущенных контейнеров:
```bash
docker stats
```

Останавливаем и удаляем контейнеры, сети, тома и образы:
```bash
docker-compose down -v
```

Команда покажет, сколько места на диске занимают образы, контейнеры, тома и билд-кеш. Будет и информация о том, сколько места можно освободить, удалив ненужное:
```bash
docker system df
```

Все неактивные (остановленные) контейнеры удаляются командой:
```bash
docker container prune
```

Можно удалить образы, какие использовались как промежуточные для сборки других образов, но на которые не ссылается ни один контейнер. Их называют dangling images (англ. «висячие образы»). Для выполнения такой задачи используется команда:
```bash
docker image prune
```
Удалить вообще всё, что не используется (неиспользуемые образы, остановленные контейнеры, тома, которые не использует ни один контейнер, билд-кеш), можно командой:
```bash
docker system prune
```

### Автор проекта:

- [Григорий Федоренко](https://github.com/GregFedy)

![](https://img.shields.io/badge/Python-3.7.0-blue?style=flat&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-3.2.16-green?style=flat&logo=django&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-13.0-orange?style=flat&logo=postgresql&logoColor=white)
[![workflow](https://github.com/GregFedy/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/GregFedy/foodgram-project-react/actions/workflows/main.yml)