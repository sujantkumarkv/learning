''' Here we wld make a bot using Selenium Webdriver that wld auto apply for jobs on linkedIn for us. simpel :)'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

chromedriver_path= 'C:\Program Files\Google\Chrome\chromedriver'
driver= webdriver.Chrome(executable_path=chromedriver_path)

LINKEDIN_URL= 'https://www.linkedin.com/jobs/search/?f_E=2&f_WRA=true&geoId=102490453&keywords=python%20developer&location=Silicon%20Valley%2C%20California%2C%20United%20States'

USERMAIL= 'kumarskv1362@gmail.com'
PASSWORD= 'LINKEDINkskv123#'

driver.get(url=LINKEDIN_URL)

try:

    sign_in_btn= driver.find_element_by_link_text('Sign in')
    sign_in_btn.click()

    email_bar= driver.find_element_by_id('username')
    email_bar.send_keys(USERMAIL)

    password_bar= driver.find_element_by_id('password')
    password_bar.send_keys(PASSWORD)
    password_bar.send_keys(Keys.ENTER)

    '''
    2ND SIGN IN ISNT NEEDED AS ENTER KEY ON PASSWORD FIELD ALSO DOES IT AS IN CODE ABOVE :)
    #sign_in_btn_2= driver.find_element_by_css_selector('.login__form_action_container button')
    #sign_in_btn_2.send_keys(Keys.ENTER)
    '''

    action= ActionChains(driver)

    jobs_list= driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul')
    print(len(jobs_list))

    jobs_save_btn= driver.find_element_by_css_selector('.jobs-details-top-card__actions span button')
    #jobs_save_btn.click()

except NoSuchElementException:
    print('No such element found or no job save option.')
