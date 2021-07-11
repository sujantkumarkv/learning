#CONSTANTS
MY_EMAIL = "yagamilight1362@gmail.com"
PASSWORD = "YAGAMIRAITOprince123#"
RECEIVER_MAIL = 'keiyagami67@gmail.com'
MY_LATITUDE= '26.727100'
MY_LONGITUDE= '88.395287'

#packages 
import requests
import smtplib
from datetime import datetime as dt
import time

#SEND MAIL IF ISS OVERHEAD & ITS DARK TO VIEW
#It checks if ISS is above us or not :)
while True:
    #but this is gonna run too frequently, so we will slow it with time module :)
    time.sleep(120) #we run it every 2 mins - 120 seconds...
    if iss_is_overhead() and is_dark():
        with smptlib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addr=RECEIVER_MAIL,
                msg='Subject: LOOK UP AT THE ISS \n\n The ISS is above you bruh.. GET UP & see THE BEAUTY'
            )


#************** SUNRISE, SUNSET TIMINGS PART SINCE ISS IS VISIBLE ONLY IF ITS DARK , ofc bruh :) ***************
def is_dark(): 
    lat_long_params= {
        'lat': MY_LATITUDE,
        'lng': MY_LONGITUDE,
        'formatted': 0, #its given in API'S documentation, this sets the result in 24hr format .   
    }

    sunrise_sunset_response = requests.get('https://api.sunrise-sunset.org/json', params=lat_long_params)
    sunrise_sunset_data= sunrise_sunset_response.json()

    sunrise= int(sunrise_sunset_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset= int(sunrise_sunset_data['results']['sunset'].split('T')[1].split(':')[0])

    print(sunrise)
    print(sunset)
    #print(sunrise_sunset_data)
    now= dt.now()
    #print(now.hour)

    #now if we gonna watch iss, we ensure that it's dark.
    if now.hour>=sunset or now.hour<=sunrise:
        return True
    else:
        return False

#**************************************************************************************************************

def iss_is_overhead():
    try:
        response= requests.get('http://api.open-notify.org/iss-now.json')

    except:
        print(response.raise_for_status) #raises the exception :)
    
    data= response.json()
    latitude= float(data['iss_position']['latitude'])
    longitude= float(data['iss_position']['longitude'])
    location= (latitude, longitude)
    #print(location)

    if latitude-7 <= MY_LATITUDE <= latitude+7 and longitude-7 <= MY_LATITUDE <= longitude+7:
        return True
    else:
        return False
    
    