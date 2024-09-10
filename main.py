import requests
from datetime import datetime
import smtplib
import time

my_email = "riteshbill14@gmail.com"
my_password = "usaf brwt cubo edfa"

# latitude and longitude of Hetauda, Nepal

LAT = 27.423170
LNG = 85.033679

def is_iss_overhead():
    # Getting the data of iss overhead to know its current position
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    # print(response.status_code)  # .status_code--> only gives the status code like 200,400 ....
    response.raise_for_status()
    data = response.json() # json() --> helps to get you the data

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if LAT-5 <= iss_latitude <= LAT+5 and LNG -5 <= iss_longitude <= LNG +5:
        return True

def is_night():
    parameters = {
        "lat" :LAT,
        "lng" : LNG,
        'formatted':0
    }

    # getting the data from the sunrise and sunset api and passing parameters
    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    # Getting current time
    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password= my_password)
            connection.sendmail(
                to_addrs= my_email,
                from_addr= my_email,
                msg="Subject: Look Up!!\n\n The ISS is above you in the sky."
            )

