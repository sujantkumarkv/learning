import requests

from data_manager import DataManager
SHEETY_ENDPOINT= 'https://api.sheety.co/55c0c68ec47e546f700e0968728aea6f/flightDeals/prices'

obj= DataManager()

params={
    'price': {
        'city': 'Port Blair',
        'iataCode': 'ixz', 
        'lowestPrice': 4000,
    }
}

response= requests.post(url= f"{SHEETY_ENDPOINT}/2", json=params)
print(response.text)