# 🚀 Notification Service API

A simple yet powerful notification service built with *FastAPI* and *MongoDB* to send *Email, **SMS, and **In-App* notifications. It supports background processing and retry logic to ensure robust delivery.

---

## 📌 Features

- ✅ REST API with FastAPI
- 🗃 MongoDB for data persistence
- 🔔 Notification types: email, sms, in_app
- 🎯 Background tasks for async processing
- 🔁 Retry mechanism for failed notifications
- 📦 Clean project structure with environment variable support
- 🧪 Interactive API docs via Swagger

---

## 🏗 Project Structure

notification_service/
├── app/
│ ├── main.py # Main API routes
│ ├── schemas.py # Pydantic models
│ ├── models.py # Custom MongoDB ObjectId handler
│ ├── database.py # MongoDB client setup
│ ├── config.py # Environment config loader
│ └── utils.py # Background sender logic
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🔧 Requirements

- Python 3.9+
- MongoDB (local or cloud)

---

