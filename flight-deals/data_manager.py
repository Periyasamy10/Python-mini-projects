import requests
from pprint import pprint

sheet_endpoint = "https://api.sheety.co/eabcf3619cb5f8f53efd34d4a997ac1b/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheet_endpoint}/{city['id']}",json=new_data)
            print(response.text)
