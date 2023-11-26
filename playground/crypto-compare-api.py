import requests

apiKey = "c1426ed39f4fe6ad9c78119240917d84a11a2cff08a4c5ba3391ebd5b7e38cbc"

url = "https://min-api.cryptocompare.com/data/price"

payload = {"api_key": apiKey, "fsym": "CELO", "tsyms": "USD,ZAR"}

result = requests.get(url, params=payload).json()

# print(result)
# print(type(result["USD"]))
# print(result["USD"])
# print(result["ZAR"])


# def cryptoConvert(currencyCode: str, cryptoCode: str):
#     apiKey = "c1426ed39f4fe6ad9c78119240917d84a11a2cff08a4c5ba3391ebd5b7e38cbc"

#     url = "https://min-api.cryptocompare.com/data/price"

#     payload = {"api_key": apiKey, "fsym": cryptoCode, "tsyms": currencyCode}

#     result = requests.get(url, params=payload).json()

#     return result[currencyCode]


def cryptoConvert(
    senderCurrencyCode: str, receiverCurrencyCode: str, cryptoCode: str, amount: float
):
    apiKey = "c1426ed39f4fe6ad9c78119240917d84a11a2cff08a4c5ba3391ebd5b7e38cbc"

    url = "https://min-api.cryptocompare.com/data/price"
    currencyCode = f"{senderCurrencyCode},{receiverCurrencyCode}"

    payload = {
        "api_key": apiKey,
        "fsym": cryptoCode,
        "tsyms": currencyCode,
    }

    result = requests.get(url, params=payload).json()

    final_res = round(
        (amount / result[senderCurrencyCode]) * result[receiverCurrencyCode], 2
    )

    return final_res


result = cryptoConvert("USD", "ZAR", "CELO", 500.00)
print(result)
