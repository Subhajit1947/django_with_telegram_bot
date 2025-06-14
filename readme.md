# Telegram Post Bot API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.14-red)](https://www.django-rest-framework.org/)


A robust Django backend system with Telegram bot integration for user authentication and post management.

## 🚀 Features

- 🔐 JWT Authentication (Register, Login)
- ✍️ CRUD API for Posts
- 🤖 Telegram bot integration
- 📧 Welcome email via Celery + SMTP
- 🧾 My Posts view for each authenticated user

---

## 🛠 Tech Stack

- Django
- Django REST Framework
- Celery + Redis + Flower(development) + Mailpit(Dev Email Host)
- SQLite
- Telegram Bot API
- Simple JWT

---


## 🚀 Getting Started(Locally)

### Prerequisites

- Python 3.10+
- Redis server
- Mailpit
- Telegram bot token from [@BotFather](https://t.me/BotFather)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Subhajit1947/django_with_telegram_bot
   ```
2. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate.ps1  # Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a .env file in root directory and add configuration:
    ```bash
    SECRET_KEY = ''
    EMAIL_BACKEND = ''  
    EMAIL_PORT=""
    EMAIL_HOST=""
    DEFAULT_FROM_EMAIL=""
    CELERY_BROKER_URL=''
    CELERY_RESULT_BACKEND=''
    TELEGRAM_BOT_TOKEN=''
    ```
5. Run migrations,migrate,createsuperuser:
    ```bash
    python manage.py makegirations
    python manage.py migrate
    python manage.py createsuperuser
    ```
6. Start Development Server:
    ```bash
    python manage.py runserver 0.0.0.0:8000 
    ```
7. Run Celery:
    ```bash
    celery -A config worker --pool=solo -l info
    ```
8. Create a LocalTunnel (nodejs must be install):
    ```bash
    npm install -g localtunnel 
    lt --port 8000 --subdomain mybot  
    ``` 
    after run this command you get a https url
9. Set Webhook (put https url in yourdomain)
    ```shell
    requests.post(
        "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook",
        json={"url": "https://yourdomain.com/telegram/webhook/"}
    )
    ```



---

## 🔐 Authentication Endpoints

| Endpoint         | Method | Description          |
|------------------|--------|----------------------|
| `/auth/register/`| POST   | User registration    |
| `/auth/login/`   | POST   | Obtain JWT token     |

---

## 📦 API Endpoints for Posts

| Endpoint               | Method  | Auth Required | Description                |
|------------------------|---------|----------------|----------------------------|
| `/posts/`              | GET     | No             | List all posts             |
| `/posts/create/`       | POST    | Yes            | Create a post              |
| `/posts/<id>/`         | GET     | No             | View single post           |
| `/posts/<id>/update/`  | PUT     | Yes            | Update post (owner only)   |
| `/posts/<id>/delete/`  | DELETE  | Yes            | Delete post (owner only)   |
| `/me/posts/`           | GET     | Yes            | List user's own posts      |

---

## 🤖 Telegram Bot

- Users are registered via `/start` command.
- Registered Telegram users are saved in the DB.
- Welcome message is sent via `sendMessage`.

