from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path= 'C:\Program Files\Google\Chrome\chromedriver'
driver= webdriver.Chrome(executable_path=chromedriver_path)

COOKIE_CLICKER_URL= "http://orteil.dashnet.org/experiments/cookie/"

driver.get(COOKIE_CLICKER_URL)

clickable_cookie= driver.find_element_by_id('bigCookie')

timeout = time.time() + 5
five_min = time.time() + 300

while True:
    clickable_cookie.click()
    store = driver.find_elements_by_css_selector('#store div')

    if time.time() >= buy_item_timeout:
        try:
            upgrade = [upgrade for upgrade in store if
                       upgrade.get_attribute('class') != 'grayed' and upgrade.get_attribute(
                           'class') != 'amount'][-1]
        except IndexError:
            pass
        else:
            upgrade_price = upgrade.text.splitlines()[0].split(' ')[2]
            money = driver.find_element_by_id('money').text
            if int(money) > int(upgrade_price):
                print(f'upgrade price: {upgrade_price}\n money : {money}')
                upgrade.click()
        buy_item_timeout = time.time() + 5

    if time.time() >= game_timeout:
        break

cps = driver.find_element_by_id('cps').text
print(cps)