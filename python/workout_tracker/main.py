import os
import requests
from datetime import datetime as dt

#1. ENTER IN PLAIN ENGLISH, here repl.it
DATA_ENDPOINT= 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_ENDPOINT= os.environ['SHEET_ENDPOINT'] #Its 4 POST.


data_headers= {
    'x-app-id': os.environ['DATA_APP_ID'],
    'x-app-key': os.environ['DATA_APP_KEY'],
}

q= input('Tell about todays workout u did :\n')

#date and time
date_now= dt.now().strftime('%d/%m/%Y')
time_now= dt.now().strftime('%H:%M:%S')

#####
data_params= {
    'query': q,   
}

data_response= requests.post(
  url=DATA_ENDPOINT, 
  json=data_params, 
  headers=data_headers)

exercises_data= data_response.json()['exercises']

for exercise in exercises_data:
    
    #3. TAKE OUT THE FEATURES & CALL THE NUTRITRIONIX API for the relevant data
    sheety_params= {
        'workout': {
            #THE TIME IS IN UTC, this time +5:30 = my time.
            'date': date_now,
            'time': time_now,
            "duration": exercise["duration_min"],
            'exercise': exercise['name'],
            'calories': exercise['nf_calories'],   
        }
    }

    #Bearer Token
    sheety_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
    }

    #4. UPDATE RESULT IN SHEETS with relevant data
    sheety_response= requests.post(
      url=SHEETY_ENDPOINT, 
      json=sheety_params,
      headers=sheety_headers,
      )

    print(sheety_response.text)
    print(sheety_response.status_code)   
    
# BOOM DONE !!