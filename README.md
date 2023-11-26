# Remmitance Comparison Application

## Description
Remittances to and within Africa are expensive and slow. For instance, the average cost of a remittance to Africa is about 9%, and it can take several days for the money to arrive. This is a major problem for Africans who rely on remittances from family and friends living abroad. Blockchain has enabled users to invest, purchase, and send money via cryptocurrencies. Therefore, there is a potential for individuals to send money in the form of cryptocurrencies. 

## Objective of this project
The aim of this project is to build a simple web based application that compares the cost of remittance using cryptocurrency as opposed to sending money using the ‘traditional’ method (e.g. World Remit, Wise, Moneygram, etc)



### Setup Instructions
1. It is highlty recommended that you create a Python Virtual Environment before installing dependencies and running the server locally.

2. To run the python server locally, first install the following Python packages:
```
pip install fastapi[all]
```

3. Next run `uvicorn main:app` to start the server locally.

4. Once the server is running, navigate to `http://127.0.0.1:8000/docs#/`, as this opens an interactive FAST API docs for this project.