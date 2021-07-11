 
''' WE WANT HOURLY RAIN DATA FOR say,12 HRS (the working hours), CODE RUNS
    IN MORNING say,7am & send us a message if data says chances of rain '''

import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

#CONSTANTS
MY_LATITUDE= 26.727100
MY_LONGITUDE= 88.395287

API_KEY= 'dcf746d70f5a64446bb964bc81a439d2'
WEATHER_ENDPOINT= 'https://api.openweathermap.org/data/2.5/onecall'

''' ENVIRONMENT VARIABLES'''
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']

account_sid= 'AC0b98a26f774daea0eb6c53c05dbc8c8d'
auth_token= 'ea5abe2e0197c8e12cce6d0cadbbc47e'

weather_parameters={
    'lat': MY_LATITUDE,
    'lon': MY_LONGITUDE,
    'appid': API_KEY,
}

response= requests.get(WEATHER_ENDPOINT, params=weather_parameters)
response.raise_for_status()

raining= False

weather_data= response.json()
''' The documentation says that if weather ID <700 we have some kind of rain chances ..'''

weather_data_slice= weather_data['hourly'][:18] #takes 12 hours data, well we can obvio change it

for hourly_data in weather_data_slice:

    #print(weather_data['hourly'][i]['weather'][0]['id'])
    if hourly_data['weather'][0]['id'] < 700:
        raining= True

if raining:
    # Download the helper library from https://www.twilio.com/docs/python/install
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    ''' I WROTE THE BELOW CODE ONLY BCZ I HOSTED ON pythonanywhere.com & it's there issue since I use a free account.
        If i pay, i get a dedicated location address but for now I get a proxy so gotta MODIFY CODE ACCORDING TO IT
        SO THAT IT WORKS else this {proxy_client} thing is not needed '''
    proxy_client= TwilioHttpClient()
    proxy_client.session.proxies= {'https': os.environ['https_proxy']}


    client = Client(account_sid, auth_token, http_client= proxy_client)

    message = client.messages \
                    .create(
                        body="carry Umbrella",
                        from_='+19256848983',
                        to='+918538834886'
                    )

    print(message.status)



        