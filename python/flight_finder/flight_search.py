import requests

KIWI_LOCATIONS_ENDPOINT= "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT= "https://tequila-api.kiwi.com/v2/search"
KIWI_API_KEY= '6n1imXODPxS0medCcPSaFjFSpSOv1Tf3'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
        
    def get_iata_code(self, city):
        
        kiwi_locations_params={
          'term': city,
          'location_types': 'city',
        }
        kiwi_locations_headers={
            'apiKey': KIWI_API_KEY,
        }
        iata_response= requests.get(url=KIWI_LOCATIONS_ENDPOINT, params=kiwi_locations_params, headers=kiwi_locations_headers)
        iata_code= iata_response.json()['locations'][0]['code']
        return iata_code
    