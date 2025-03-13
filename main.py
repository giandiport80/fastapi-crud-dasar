from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from app.handlers.handler import validation_exception_handler
from app.modules.user import user_route

app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(user_route.router)

@app.get("/", status_code=200)
def main():
    return {
            "message": "Hello world"
        }