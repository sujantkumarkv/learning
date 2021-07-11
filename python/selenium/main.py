from selenium import webdriver

chromedriver_path= 'C:\Program Files\Google\Chrome\chromedriver'
driver= webdriver.Chrome(executable_path=chromedriver_path)


URL2= 'https://www.python.org/'
driver.get(URL2)


price= driver.find_element_by_id('priceblock_ourprice')
print(price.text)

link= driver.find_element_by_xpath('//*[@id="navFooter"]/div[5]/table/tbody/tr[1]/td[3]/a')
print(link.text)

events_time= driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
for i in events_time:
    print(i.text)
#The above code just doesn't work, it does print all the dates & names but all in diff lines &
#its kinda all elements as a single element separated by \n(I saw pattern when printed it using split(" "))
#so wld have find_by_css_selectors as used by Angela mam in vid.

#events= dict(zip(events_time, events_name))


'''I GOTTA TAKE IN DATA FROM python.org site & pull in the latest events' date,names & STACK THEM .
    In the lines above, I did mistake of putting in XPATH of only 1st element & the code above basically 
    simply uses list comprehension to loop in for the event time/date & zip(key, value) feature . Its great function.
'''

events_time= driver.find_elements_by_css_selector('.event-widget time')
events_name= driver.find_elements_by_css_selector('.event-widget li a') #not putting <li> wld give "More" link too in the page.

events= dict(zip((event_time.text for event_time in events_time), (event_name.text for event_name in events_name)))
print(events)

driver.close()