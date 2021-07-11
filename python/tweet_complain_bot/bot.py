from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

USERNAME= 'sujantkumarkv'
PASS= 'TWITTERkskv123#'

class TwitterBot:
    def __init__(self, chromedriver_path, option):
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)
        self.driver.maximize_window()

    def get_internet_speed(self):
        SPEEDTEST_URL= 'https://www.speedtest.net'
        self.driver.get(SPEEDTEST_URL)
        go_btn= self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()
        time.sleep(60)
        
        down_speed= self.driver.find_element_by_class_name('download-speed').text
        up_speed= self.driver.find_element_by_class_name('upload-speed').text
        return (down_speed, up_speed) #ITS A TUPLE,We can access elements down_speed, up_speed from [0] & [1]

    def tweet_provider(self, msg):
        TWITTER_URL= 'https://www.twitter.com/login'
        self.driver.get(url=TWITTER_URL)
        time.sleep(1)

        # logging
        username_bar= self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username_bar.send_keys(USERNAME)

        password_bar= self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password_bar.send_keys(PASS)
        time.sleep(1)
        password_bar.send_keys(Keys.ENTER)

        # posting
        tweet_btn= self.driver.find_element_by_link_text('Tweet')
        tweet_btn.click()

        tweet_box= self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(msg)

        tweet_btn_2= self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        tweet_btn_2.click()
