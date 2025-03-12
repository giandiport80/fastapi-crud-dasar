from fastapi import FastAPI
from starlette.responses import JSONResponse
from app.modules.user import user_route

app = FastAPI()

app.include_router(user_route.router)

@app.get("/")
def main():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Hello world"
        }
    )