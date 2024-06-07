import requests
from flight_data import FlightData
from pprint import pprint

TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILLA_KEY = "_2ABNKfe3_8uhdJ1xMTP7Gi01zHmpv4-"
location_endpoint = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    def __init__(self):
        self.city_codes=[]

    def get_destination_code(self, city_name):
        print("get destination code trigred")
        location_endpoint = "https://api.tequila.kiwi.com/locations/query"
        headers = {"apikey": TEQUILLA_KEY}
        for city in city_name:
            query = {"term": city, "location_types": "city"}
            response = requests.get(url=location_endpoint, params=query, headers=headers)
            result = response.json()["locations"]
            code = result[0]["code"]
            self.city_codes.append(code)
        return self.city_codes

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey": TEQUILLA_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=location_endpoint, params=query, headers=header)

        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code}:{data['price']}")
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=location_endpoint,
                headers=header,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
