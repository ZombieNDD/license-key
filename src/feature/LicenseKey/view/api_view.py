from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from feature.LicenseKey.entity.license_key_entity import FeatureResponse, LoginRequest, LoginResponse
from viewmodel.license_key_viewmodel import LicenseKeyViewModel

class LicenseAPIView:
    def __init__(self):
        self.viewmodel = LicenseKeyViewModel()
        self.router = APIRouter()
        self.router.post("/auth", response_model=LoginResponse)(self.auth)
        self.router.get("/features/{key}", response_model=FeatureResponse)(self.features)

    def auth(self, request: LoginRequest):
        return self.viewmodel.login(request)

    def features(self, key: str, device_id: str):
        return self.viewmodel.get_features(key, device_id)