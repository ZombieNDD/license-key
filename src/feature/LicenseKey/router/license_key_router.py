from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
router = APIRouter()

@router.post("/auth")
def auth_endpoint():
    pass

@router.get("/features/{key}")
def features_endpoint():
    pass
