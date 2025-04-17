import time

import requests
from datetime import datetime
import smtplib
import time
my_email = "tarun96968@gmail.com"
my_password= "srcv nbae lpoh fhxd"

# form https://www.latlong.net/Show-Latitude-Longitude.html  I gt my location
MY_LAT = 25.317644 # Your latitude
MY_LONG = 82.973915 # Your longitude

# this function tell us out position is same of ISS satellite position or not
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LONG-5)<= iss_longitude<=(MY_LONG+5) and (MY_LAT-5)<=iss_latitude<=(MY_LAT+5):
        return True
# this function tell us our current position is in night time or not
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  #  this will give our time of sunset,sunrise in 24 hour format
    }
# https://sunrise-sunset.org/api   from here we sunset,sunrise API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour


    if time_now>=sunset or time_now <= sunrise: # this condition for checking it dark night or not
        return  True

#we only get message if our satellite is our location and in must in dark night time
while True:
    time.sleep(60)  # BONUS: run the code every 60 seconds.
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look Up👆\n\n This ISS is above you in the sky."
        )


#for continuous running  and getting notification we have to either host this program or we have open this console in run position for one day"""




