from datetime import datetime
from pydantic import BaseModel

class LoginRequest(BaseModel):
    key: str
    device_id: str

class LoginResponse(BaseModel):
    message: str
    features: dict
    expires_at: datetime

class FeatureResponse(BaseModel):
    features: dict