from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from bigger_app.items.routers import router as items_router
from bigger_app.users.routers import router as users_router
from bigger_app.admin.routers import router as internal_router

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(
    users_router,
    prefix="/users"
)
app.include_router(
    items_router,
    prefix="/items"
)
app.include_router(
    internal_router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
