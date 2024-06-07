import requests
from datetime import datetime

TOKEN = "thisissecret"
USERNAME = "periyasamy"
pixela_endpoint = "https://pixe.la/v1/users"

parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=parameter)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)


value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2022,month=9,day=12)

value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.5",
}

#response = requests.post(url=value_endpoint, json=value_config, headers=headers)

update_endpoint = f"{value_endpoint}/{20220914}"

update_config={
    "quantity":"2.5"
}

#response = requests.put(url=update_endpoint,json=update_config,headers=headers)

response = requests.delete(url=update_endpoint,headers=headers)
