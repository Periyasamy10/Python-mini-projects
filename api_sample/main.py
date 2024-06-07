import requests
from datetime import datetime
from twilio.rest import Client
import html

# # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()
# # data = response.json()
# #
# # print(data)
# #
# # latitude = data["iss_position"]["latitude"]
# # longitude = data["iss_position"]["longitude"]
# #
# # position = (latitude,longitude)
# #
# # print(position)
# MY_LAT = 10.960078
# MY_LON = 78.076607
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LON,
#     "formatted":0,
# }
# response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
#
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#
# now = datetime.now()
#
#
# print(sunrise)
# print(sunset)
#
# print(now.hour)


# parameters = {
#     "lat": 10.960078,
#     "lon": 78.076607,
#     "appid": "81e71775e049d1d372794c6c922f4fcd",
# }
# response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
# data = response.json()
# print(data['weather'][0]['id'])
#
# account_sid = "AC76dceec63258dd8f342c5e561173e730"
# auth_token = "ba3fb2316e6cf593de366a017d542939"
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body="Hii my first msg through progr am",
#                      from_='+16185912647',
#                      to='+918220997661'
#                  )


NEWS_API_KEY = "0ce1cac5092a477eb972f986cefcbf8c"
parameter = {
    "q":"Tesla Inc",
    "apikey":NEWS_API_KEY,
    "language":"en",
    "sortBy":"publishedAt",
}

response = requests.get("https://newsapi.org/v2/everything",params=parameter)
data = response.json()
data_slice = data["articles"][:3]
for num in data_slice:
    heading = num["title"]
    description = num["description"]
    print(html.unescape(heading))
    print(html.unescape(description))




















