from selenium import webdriver
from bot import TwitterBot

chromedriver_path= 'C:/Program Files/Google/Chrome/chromedriver'
brave_path= 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

option= webdriver.ChromeOptions()
option.binary_location= brave_path

MIN_DOWN= 21
MIN_UP= 21
bot = TwitterBot(chromedriver_path, option)
current_speeds = bot.get_internet_speed() #current_speeds is a returned tuple

down = float(current_speeds[0])
up = float(current_speeds[1])

if down < MIN_DOWN or up < MIN_UP:
    print(f'down: {down}\nup{up}')
    tweet = f'DISCLAIMER: ITS A SAMPLE TWEET LEARNING WEB AUTOMAION Hi @JioCare \
    @reliancejio, my internet speed is {down}DOWN/{up}UP instead of {MIN_DOWN}DOWN/{MIN_UP}up'
    bot.tweet_provider(msg=tweet)
