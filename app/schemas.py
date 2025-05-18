from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.models import PyObjectId


class NotificationCreate(BaseModel):
    user_id: str
    type: str  # "email", "sms", "in-app"
    title: str
    message: str


class NotificationOut(NotificationCreate):
    id: Optional[PyObjectId]

    model_config = ConfigDict(arbitrary_types_allowed=True)

class Notification(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_id: str
    type: str  # "email", "sms", or "in-app"
    title: str
    message: str
    status: str = "pending"  # default status

    class Config:
        json_encoders = {ObjectId: str}  # Optional: helpful when returning MongoDB IDs as JSON