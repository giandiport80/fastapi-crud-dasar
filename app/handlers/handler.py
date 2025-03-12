from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom Validation Error Handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}

    for error in exc.errors():
        field_name = error["loc"][-1]  # Nama field
        message = error["msg"]  # Pesan error

        # Simpan error dalam dictionary dengan format Laravel
        if field_name in errors:
            errors[field_name].append(message)
        else:
            errors[field_name] = [message]

    return JSONResponse(
        status_code=422,
        content={
            "message": "The given data was invalid.",
            "errors": errors
        }
    )

