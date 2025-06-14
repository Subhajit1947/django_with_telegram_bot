# 🧠 Telegram Post Bot API

A Django-based platform integrated with a Telegram bot that allows users to register, log in, and manage posts. It uses Celery for background tasks like sending welcome emails and JWT for secure authentication.

---

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

### Set Webhook
```shell
requests.post(
    "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook",
    json={"url": "https://yourdomain.com/telegram/webhook/"}
)
```
### 📧 Celery Email Task

A welcome email is sent automatically when a new user registers using the registration API.

### 🟢 Run Celery

```bash
celery -A config worker --pool=solo -l info

