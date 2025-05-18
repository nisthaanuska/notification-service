from bson import ObjectId
from pydantic import BaseModel, Field
from pydantic import ConfigDict
from typing import Optional


class PyObjectId(ObjectId):
    @classmethod
    def _get_validators_(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def _modify_schema_(cls, field_schema):
        field_schema.update(type="string")


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