"""
Entry point for the Remittence Calculator server.
"""
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from common.actions import ConvertAmount, ConvertResult
from common.operations import convertAmount


# from settings import AppSettings

# app_settings = AppSettings()

# origins = [str(app_settings.primary_origin)]
# if app_settings.staging_mode:
#     origins.append("http://localhost:4200")

origins = ["*"]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["GET", "POST", "HEAD", "DELETE"],
    allow_headers=["*"],
)


@app.post("/convert", response_model=ConvertResult, status_code=status.HTTP_201_CREATED)
async def post_convert_amount(request: ConvertAmount) -> ConvertResult:
    return convertAmount(request)
