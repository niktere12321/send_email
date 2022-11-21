# Проект send_email

## Описание

send_email это сервис для отправки электронной почты.

Пользователи могут:
- создать макет письма и отправить подписчикам на выбор;
- отправить отложенные письма;
- использовать переменные в макете;
- отслеживанть открытие писем.

## Технологии
- Python 3.7.9
- Django 2.2.28

## Установка проекта локально

* Склонировать репозиторий на локальную машину:
```bash
git clone https://github.com/niktere12321/send_email.git
```
```bash
cd send_email
```

- Создать и заполнить по образцу .env-файл
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=example_password
SECRET_KEY=f($n-01g^9gt^@03$%wjjoea_jvfo8-p21_!3#ahi+v@!5urnq
TELEGRAM_TOKEN=TELEGRAM_TOKEN
CHAT_ID=CHAT_ID
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

* Выполните миграции:
```bash
cd send_email
```
```bash
python manage.py migrate
```

* Запустите сервер:
```bash
python manage.py runserver
```

* Во втором терминале запустить Celery в директории где находиться manage.py предварительно запустив Redis:
```bash
celery -A send_email worker -l info -P gevent
```

---
## Техническая информация

Стек технологий: Python 3, Django, Django Rest, Docker, PostgreSQL, nginx, gunicorn, Djoser.

---
## Об авторе

Терехов Никита Алексеевич
