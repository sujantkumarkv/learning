import requests

#class Data:
    
#    def __init__(self):
#        self.parameters={
#            'amount': 45,
#            'type': "boolean",
#        }
#        self.data= requests.get('https://opentdb.com/api.php', params= self.parameters).json()
#        self.question_data= self.data['results']
#        return self.question_data

parameters={
    'amount': 45,
    'type': "boolean",
    }
response= requests.get('https://opentdb.com/api.php', params= parameters)
response.raise_for_status()
data= response.json()
question_data= data['results']

#return question_data

