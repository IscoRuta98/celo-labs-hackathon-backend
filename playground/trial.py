import requests
from common.actions import ConvertAmount, ConvertResult, ConvertAmountSuccess


def convertAmount(request: ConvertAmount):
    cryptoAmount = cryptoConvert(
        senderCurrencyCode=request.senderCurrencyCode,
        receiverCurrencyCode=request.receiverCurrencyCode,
        cryptoCode=request.cryptoCurrencyCode,
        amount=request.amount,
    )
    print(cryptoAmount)

    remittenceProviders = fiatConvert(
        senderCurrency=request.senderCurrencyCode,
        amount=request.amount,
        receiverCurrency=request.receiverCurrencyCode,
    )

    result = ConvertAmountSuccess(
        cryptoAmount=cryptoAmount, providers=remittenceProviders
    )

    return result


def cryptoConvert(
    senderCurrencyCode: str, receiverCurrencyCode: str, cryptoCode: str, amount: float
):
    apiKey = "c1426ed39f4fe6ad9c78119240917d84a11a2cff08a4c5ba3391ebd5b7e38cbc"

    url = "https://min-api.cryptocompare.com/data/price"
    currencyCode = f"{senderCurrencyCode},{receiverCurrencyCode}"
    print(currencyCode)

    payload = {
        "api_key": apiKey,
        "fsym": cryptoCode,
        "tsyms": currencyCode,
    }

    result = requests.get(url, params=payload).json()

    # Extract the conversion rates
    sender_rate = result.get(senderCurrencyCode)
    receiver_rate = result.get(receiverCurrencyCode)

    if sender_rate is None or receiver_rate is None:
        raise ValueError("Invalid currency codes provided")

    # Calculate the final result
    print(sender_rate)
    print(receiver_rate)
    final_res = round((amount / sender_rate) * receiver_rate, 2)
    print(final_res)

    return final_res


def fiatConvert(senderCurrency, amount, receiverCurrency):
    url3 = f"https://api.wise.com/v3/comparisons?sourceCurrency={senderCurrency}&targetCurrency={receiverCurrency}&sendAmount={amount}"

    headers = {"accept": "application/json"}

    response = requests.get(url3, headers=headers)
    data = response.json()

    # Extract providers array
    providers = data.get("providers", [])

    # List of providers to include
    included_providers = ["ofx", "wise", "remitly"]

    # Initialize a list to store the extracted information
    extracted_info = []

    # Iterate through each provider and extract required information
    for provider in providers:
        alias = provider.get("alias")
        name = provider.get("name")

        # Check if the provider is in the list of included providers
        if alias in included_providers:
            # Extract the first quote
            quotes = provider.get("quotes", [])
            if quotes:
                first_quote = quotes[0]
                rate = first_quote.get("rate")
                fee = first_quote.get("fee")
                received_amount = first_quote.get("receivedAmount")

                # Include alias in the extracted information
                info = {
                    "Provider": name,
                    "Rate": rate,
                    "Fee": fee,
                    "Received Amount": received_amount,
                }

                # Append the information to the list
                extracted_info.append(info)

    return extracted_info


test = ConvertAmount(
    amount=500.00,
    senderCurrencyCode="USD",
    cryptoCurrencyCode="CELO",
    receiverCurrencyCode="ZAR",
)

test_result = convertAmount(test)
print(test_result)
