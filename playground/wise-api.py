import requests

url2 = "https://wise.com/gateway/v3/comparisons?midMarketRate=18.7828&payInMethod=DIRECT_DEBIT&sendAmount=100&sourceCurrency=USD&targetCurrency=ZAR&wiseFee=6.59"
url3 = "https://api.wise.com/v3/comparisons?sourceCurrency=USD&targetCurrency=ZAR&sendAmount=100"

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

# Print or process the extracted information as needed
for info in extracted_info:
    print(f"Provider: {info['Provider']}")
    print(f"Rate: {info['Rate']}")
    print(f"Fee: {info['Fee']}")
    print(f"Received Amount: {info['Received Amount']}")
    print("-" * 20)

print("-" * 20)
print(extracted_info)


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


print("-" * 20)

result = fiatConvert("USD", 100.00, "ZAR")
print(result)
print(type(result))
