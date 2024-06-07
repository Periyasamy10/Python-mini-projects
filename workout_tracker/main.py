import requests
from datetime import datetime
import os
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "M"
WEIGHT_KG = 64
HEIGHT_CM = 164
AGE = 25

exercise_text = input("Tell the exercise you did? ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrition_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=ENDPOINT, json=nutrition_parameters, headers=header)
data = response.json()

sheet_endpoint = "https://api.sheety.co/eabcf3619cb5f8f53efd34d4a997ac1b/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
USERNAME = "periyasamy"
PASSWORD = "rpsachins07"

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME,PASSWORD))

    print(sheet_response.text)
