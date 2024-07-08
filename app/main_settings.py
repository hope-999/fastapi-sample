from fastapi import FastAPI

from .settings2 import settings

app = FastAPI()


@app.get("/user_info")
async def user_info():
    return {
        "user_name": settings.user_name,
        "user_email": settings.user_email,
        "user_phone": settings.user_phone,
    }
