from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def main():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Hello world"
        }
    )