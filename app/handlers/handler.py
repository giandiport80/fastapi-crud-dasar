from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        field_name = error["loc"][-1]
        message = error["msg"]
        errors.append(f"{field_name}: {message}")

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": "The given data was invalid.",
            "errors": errors
        }
    )

