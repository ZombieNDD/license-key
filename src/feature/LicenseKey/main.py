from fastapi import FastAPI
from view.api_view import LicenseAPIView

app = FastAPI()

license_controller = LicenseAPIView()
app.include_router(license_controller.router, prefix="/license")
