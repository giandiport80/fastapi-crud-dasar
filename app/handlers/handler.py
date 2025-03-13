from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import re

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
            "message": "Data yang dikirimkan tidak valid atau tidak lengkap.",
            "errors": errors
        }
    )


def validate_no_html(value: str) -> str:
    """Pastikan field tidak mengandung tag HTML"""
    if re.search(r"<[^>]*>", value):
        raise ValueError("Tidak boleh mengandung tag HTML")
    return value