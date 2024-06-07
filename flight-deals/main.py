from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
ORIGIN_CITY = "LON"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data=data_manager.get_destination_data()

destinations={
    data["iataCode"]:{
        "id": data["id"],
        "city":data["city"],
        "price":data["lowestPrice"]
    }for data in sheet_data
}

tomorrow = datetime.now() + timedelta(days=1)
six_months_after_today = datetime.now() + timedelta(days=180)

for destination_code in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY,
        destination_code,
        from_time=tomorrow,
        to_time=six_months_after_today,
    )
    if flight is not None and flight.price < destinations[destination_code]["price"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        ######################
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        #######################

        notification_manager.send_sms(message)
