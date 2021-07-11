#This class is responsible for talking to our SPREADSHEET.
import requests
from flight_search import FlightSearch

SHEETY_ENDPOINT= 'https://api.sheety.co/55c0c68ec47e546f700e0968728aea6f/flightDeals/prices'

class DataManager:

    def get_data(self):  
        return requests.get(url=SHEETY_ENDPOINT).json()['prices']        
        
    def update_sheet(self, city, row_no):   
        '''
        a=['a', 'v', 'd', 'e', 'x']
        for i in range(len(a[1:])):
            print (i+2) 
            
            BUT IT'S NOT the best way, since row_no+2 actually gives the row no & confusing to access elements,
            better way to loop through rows in sheet_data. :)
        '''    
        #THATS HOW WE ACCESS ROWS INDEX IN SHEET SINCE WE HAVE 1ST row as name
        flight_search_obj= FlightSearch()
        sheet_params={
            'price':{
                'iataCode': flight_search_obj.get_iata_code(city),                
            }
        }
        update_response= requests.put(url= f"{SHEETY_ENDPOINT}/{row_no}", json=sheet_params)
        print(update_response.text)       
