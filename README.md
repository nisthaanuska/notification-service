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

### 🏗 Project Structure


notification-service/
│
├── app/
│   ├── main.py                    # FastAPI app entry point
│   ├── models.py                  # MongoDB models and PyObjectId
│   ├── schemas.py                 # Pydantic schemas
│   ├── database.py                # MongoDB connection logic
│   ├── config.py                  # Loads environment variables
│
├── .env                           # Environment variables file
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation



---

## 🔧 Requirements

- Python 3.9+
- MongoDB (local or cloud)

---

