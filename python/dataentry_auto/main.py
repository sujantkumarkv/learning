from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from lxml import html
import time

## TODO: SCRAP DATA FROM SITE & SAVE IT IN LISTS :)
ZILLOW_URL= 'https://bit.ly/3vNbY3J' #URL is shortened.
zillow_auth_headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}
response= requests.get(url=ZILLOW_URL, headers=zillow_auth_headers)

zillow_webpage= response.text
soup= BeautifulSoup(zillow_webpage, "html.parser")
tree = html.fromstring(response.content) #jugaad soln found

#price_tags= temp.xpath('/html/body/div[1]/div[5]/div/div/div/div[1]/ul/li[1]/article/div[1]/div[2]/div/text()')
''' wrong attempts :
for price_tag in price_tags:
    property_prices.append(price_tag.getText)
'''

property_prices= tree.xpath('//div[@class="list-card-price"]/text()') #This is returned a list directly :)
property_locations= tree.xpath('//address[@class="list-card-addr"]/text()')
#links= tree.xpath('//a[@class="list-card-link"]/@href') THIS WAY I GOT A FEW LINKS ONLY; DK WHY
links= soup.select(".list-card-top a") #sugoi this works.
property_links= []

'''
print(type(links[0])) #<class 'bs4.element.Tag'>
print(type(links[0]['href'])) #<class 'str'> GIVES THE LINK REQ.
'''
for link_element in links:
    link= link_element['href']
    if "http" not in link:
        property_links.append(f'https://www.zillow.com{link}')
    else:
        property_links.append(link)
    '''
    #This logic has some issue as to it returned only a few links, not all. DK WHY.
    for i in range(21): #Since the length of 'https://www.zillow.com' is "21".
        str+= link[i]
    if str != 'https://www.zillow.com':
        link= 'https://www.zillow.com' + link
    property_links.append(link)
    str= ''
'''

'''#####################################################################'''

## TODO: USE SELENIUM TO AUTOMATE FORM-FILLING
chromedriver_path= 'C:/Program Files/Google/Chrome/chromedriver'
brave_path= 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

option= webdriver.ChromeOptions()
option.binary_location= brave_path

driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)
FORM_URL= 'https://bit.ly/3wTWT0n' #shortened URL

for n in range(len(property_links)):
    driver.get(FORM_URL)
    time.sleep(1)

    address= driver.find_element_by_xpath(
        '/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]\
        /div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]\
        /div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]\
        /div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('/html/body/div/div[3]/form\
                                                 /div[2]/div/div[3]/div[1]/div/div/span/span')

    address.send_keys(property_locations[n])
    price.send_keys(property_prices[n])
    link.send_keys(property_links[n])
    submit_button.click()
