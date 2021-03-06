import requests
import os
from twilio.rest import Client

account_sid = "**********************"
auth_token = "**********************"

api_keys = "**************************"
owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameter = {
    "lat": "49.256599",  # "29.583700", my location
    "lon": "4.033090",  # 80.215302",
    "appid": api_keys,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=owm_endpoint, params=parameter)
weather_data = response.json()

data_list = weather_data["hourly"][0:12]  # apply slicing for getting 12 hour
# print(data_list[0]["weather"][0]["id"])
will_rain = False
for hour_dict in data_list:
    weather_condition_code = int(hour_dict["weather"][0]["id"])
    if weather_condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="its going to rain today plese bring umbrella",
        from_="**********",
        to="+918009854346"
    )
    print(message.status)
# use pythoneverywhere for run this code on cloud0000
