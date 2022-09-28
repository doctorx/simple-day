from fastapi import FastAPI

from .simple_day.view import router

app = FastAPI()

app.include_router(router)




