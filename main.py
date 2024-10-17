import requests
from twilio.rest import Client
import os

# SKa4e1ac3532c805113bf53910710e7f38
# Qq5kKW62132k7JxN6GeXUgK3VJNRbiL6
# +18447251998

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# in terminal, type :
# TWILIO_SID=ACea318315eb262b02f5f78a9ffbe85244
# TWILIO_API_TOKEN=a1644bc3e5cbcf24392c0bbab5f1f4f3
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_API_TOKEN")
client = Client(account_sid, auth_token)

# "253682c0bd759acfb4255d4aa08c3dd7"
weather_parameters = {
    # nyc location
    "lat": 40.730610,
    "lon": -73.935242,
    "appid": os.environ.get("OWM_API_KEY"),
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
response.raise_for_status()
data = response.json()["list"]
will_rain = False
for forecast in data:
    weather_id = forecast["weather"][0]["id"]
    # print(forecast["weather"][0]["description"])
    if weather_id < 700:
        will_rain = True
# print(response.json())
if will_rain:
    message = client.messages.create(
        body="It's going to rain today.\nRemember to bring an ☔",
        from_="whatsapp:+14155238886",
        to="whatsapp:+19515003278",
    )


