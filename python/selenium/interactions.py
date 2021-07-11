from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path= 'C:\Program Files\Google\Chrome\chromedriver'
driver= webdriver.Chrome(executable_path=chromedriver_path)

WIKI_URL= 'https://en.wikipedia.org/wiki/Main_Page'
APP_BREWERY_URL= 'https://secure-retreat-92358.herokuapp.com/'


driver.get(url=WIKI_URL)
article_no= driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
#print(article_no.text)
'''
search_bar= driver.find_element_by_css_selector('#simpleSearch input')
search_bar.send_keys('India')
search_bar.send_keys(Keys.ENTER)
'''
#NOW WE FILL FORMS with SELENIUM
driver.get(APP_BREWERY_URL)

fname_bar= driver.find_element_by_name('fName')
lname_bar= driver.find_element_by_name('lName')
email_bar= driver.find_element_by_name('email')
sign_up_btn= driver.find_element_by_css_selector('.form-signin button')

fname_bar.send_keys('Light')
lname_bar.send_keys('Yagami')
email_bar.send_keys('example@example.com')
sign_up_btn.send_keys(Keys.ENTER)
