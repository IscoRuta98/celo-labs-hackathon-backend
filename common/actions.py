from pydantic import BaseModel
from typing import Union


class ConvertAmount(BaseModel):
    """
    parameters.
    """

    amount: float
    senderCurrencyCode: str
    cryptoCurrencyCode: str
    receiverCurrencyCode: str


class ConvertAmountSuccess(BaseModel):
    """
    Return Algorand Public address & other details upon successful wallet creation.
    """

    cryptoAmount: float
    providers: list


class ConvertAmountFailed(BaseModel):
    """
    Return Failure if amount not converted.
    """

    Failed: str


ConvertResult = Union[ConvertAmountSuccess, ConvertAmountFailed]
