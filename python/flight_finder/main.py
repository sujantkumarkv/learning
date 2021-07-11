#This file will need to use the DataManager,
#FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

data_obj= DataManager()
sheet_data= data_obj.get_data()

for row in sheet_data:
    if row['iataCode'] == '' :
        data_obj.update_sheet(city=row['city'], row_no=row['id'])
        

'''  
data_obj.update_sheet()

search_obj= FlightSearch()

###############################

for row in sheet_data:
    
    row['iataCode']= search_obj.search_iata()
    '''
    

