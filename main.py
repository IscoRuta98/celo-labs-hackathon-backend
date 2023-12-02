"""
Entry point for the Remittence Calculator server.
"""
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from common.actions import ConvertAmount, ConvertResult
from common.operations import convertAmount

origins = ["http://localhost:8080", "https://crypro-remittance-comparison.netlify.app"]


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
