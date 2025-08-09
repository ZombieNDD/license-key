from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from feature.LicenseKey.entity.license_key_entity import LoginRequest, LoginResponse

class LicenseService:
    def __init__(self, db: Session):
        self.db = db

    def login(self, data: LoginRequest) -> LoginResponse:
        license_key = self.db.query(LicenseKey).filter(LicenseKey.key == data.key).first()
        if not license_key:
            raise HTTPException(status_code=404, detail="License key not found")

        if license_key.expires_at < datetime.utcnow():
            raise HTTPException(status_code=403, detail="License key expired")

        if license_key.active_device_id and license_key.active_device_id != data.device_id:
            print(f"[INFO] Forcing logout of old device: {license_key.active_device_id}")

        license_key.active_device_id = data.device_id
        license_key.last_used_at = datetime.utcnow()
        self.db.commit()

        return LoginResponse(
            message="Login successful",
            features=license_key.features,
            expires_at=license_key.expires_at
        )

    def get_features(self, key: str, device_id: str) -> FeatureResponse:
        license_key = self.db.query(LicenseKey).filter(LicenseKey.key == key).first()
        if not license_key or license_key.active_device_id != device_id:
            raise HTTPException(status_code=403, detail="Invalid session or device")

        return FeatureResponse(features=license_key.features)
