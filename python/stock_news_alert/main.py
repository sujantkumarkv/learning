import requests
from datetime import datetime as dt, timedelta 

STOCK = "TSLA"
STOCK_ENDPOINT= 'https://www.alphavantage.co/query'
STOCK_API= 'YEKZTFBLA6YNDGEM'

NEWS_ENDPOINT= 'https://newsapi.org/v2/everything'
NEWS_API= '6364db709b0f4f9d8a6e3af9ddac9f88'


''' #1. PULL IN STOCK PRICES from stock API '''

#a. get yesterday's stock price
stock_params= {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API,
}
response= requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data= response.json()['Time Series (Daily)']


#last_stock_data= stock_data['Time Series (Daily)'][f'{yesterday}']
#day_b4_last_stock_data=  stock_data['Time Series (Daily)'][f'{day_b4_yesterday}']

''' BUT AS WE see in code above, THIS IS MUCH COMPLEX BCZ THE DATA IS DICT,but if we CONVERT it into LIST
    THEN accessing yesterday's data etc wld be simple, no keys required. & that's what we are gonna do'''

#print(stock_data.items()) *.items() gives a (key, value) tuple we need data so no need of date

stock_data_list= [daily_data for (daily_date, daily_data) in stock_data.items()]
yesterday_stock= stock_data_list[0]['4. close']
day_b4_yesterday_stock= stock_data_list[1]['4. close']
#b. get day b4 yesterday's stock price 
fetch_news= False
''' #2. COMPARE '''
diff= float(yesterday_stock) - float(day_b4_yesterday_stock)
diff_abs= abs(diff)
diff_percent= (diff_abs * 100) / float(yesterday_stock)
if diff_percent > 10:

    ''' #3. PULL NEWS ARTICLES TITLE & SUMMARY FROM NEWS API '''
    #date in format yyyy-mm-dd NEEDED as req in API.
    today= dt.now().date()
    yesterday= today - timedelta(1)
    #day_b4_yesterday= today - timedelta(2)
    news_params= {
        'qInTitle': 'tesla',
        'from': str(yesterday),
        'sortedBy': 'publishedAt',
        'language': 'en',
        'apiKey': NEWS_API,
    }
    news_response= requests.get(NEWS_ENDPOINT, params=news_params)
    news_data= news_response.json()['articles']

    #WE GET MANY ARTICLES SO WHICH TO SEND, LETS TAKE THE 1ST ARTICLE each time THE CODE RUNS,say every few mins.

    news_latest= news_data[0]
    news_headline= news_latest['title']
    news_brief= news_latest['description']
    news_url= news_latest['url'] 


    #4. SEND SMS using twilio API '''
    from twilio.rest import Client
    import os
    from twilio.http.http_client import TwilioHttpClient

    TWILIO_SID= 'AC0b98a26f774daea0eb6c53c05dbc8c8d'
    TWILIO_AUTH_TOKEN= 'ea5abe2e0197c8e12cce6d0cadbbc47e'

    '''
    proxy_client= TwilioHttpClient()
    proxy_client.session.proxies= {'https': os.environ['https_proxy']}
    '''

    #client = Client(account_sid, auth_token, http_client= proxy_client)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def stock_up(diff):
        if diff > 0:
            return '🔼'
        else:
            return '🔻' 
        
    arrow= stock_up(diff)

    msg_content= f"\n\nTSLA {arrow}{round(diff_percent)}% \n\nHeadline:{news_headline} \n\n{news_brief} \n\nRead more: \n{news_url}"

    message = client.messages.create(
                        body=msg_content,
                        from_='+19256848983',
                        to='+918538834886'
                    )

    print(message.status)



