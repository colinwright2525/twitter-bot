from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from internet_speed import InternetSpeedTwitterBot

PROMISED_DOWN = 300
PROMISED_UP = 10
CHROME_DRIVER_PATH = r'C:\Users\colin\Desktop\chromedriver'
TWITTER_EMAIL = 'bhill2846@gmail.com'
TWITTER_PASSWORD = 'Fifamaster13'

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH, PROMISED_DOWN, PROMISED_UP)
# speeds = bot.get_internet_speed()
speeds = ['down: 21.13', 'up: 11.76']

bot.tweet_at_provider(speeds, PROMISED_DOWN, PROMISED_UP, TWITTER_EMAIL, TWITTER_PASSWORD)
