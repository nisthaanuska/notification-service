from fastapi import FastAPI, HTTPException, BackgroundTasks
from app.database import notifications_collection
from app.schemas import NotificationCreate, NotificationOut
from app.utils import send_with_retry
from bson import ObjectId

app = FastAPI()

@app.post("/notifications", response_model=NotificationOut)
async def create_notification(notification: NotificationCreate, background_tasks: BackgroundTasks):
    if notification.type not in ["email", "sms", "in_app"]:
        raise HTTPException(status_code=400, detail="Invalid notification type")

    doc = notification.dict()
    doc["status"] = "pending"
    result = await notifications_collection.insert_one(doc)
    doc["_id"] = result.inserted_id

    async def process_notification(notification_id):
        notif = await notifications_collection.find_one({"_id": notification_id})
        success = await send_with_retry(notif["type"], notif["content"])
        await notifications_collection.update_one(
            {"_id": notification_id},
            {"$set": {"status": "sent" if success else "failed"}}
        )

    background_tasks.add_task(process_notification, result.inserted_id)
    return doc

@app.get("/users/{user_id}/notifications", response_model=list[NotificationOut])
async def get_user_notifications(user_id: int):
    cursor = notifications_collection.find({"user_id": user_id})
    return [doc async for doc in cursor]