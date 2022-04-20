import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:
    def __init__(self, driver_path, down, up):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/result/12912894429')

        time.sleep(5)
        start_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()

        time.sleep(60)
        download_speed = (self.driver.find_element_by_css_selector('.download-speed')).text
        upload_speed = (self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')).text
        speeds = [f'down: {download_speed}',f'up: {upload_speed}']
        self.driver.quit()
        return speeds

    def tweet_at_provider(self, speeds, prom_up, prom_down, twit_email, twit_password):
        self.driver.get('https://www.twitter.com')
        message = f'Hey Internet Provider, why is my internet speed {speeds[0]}/{speeds[1]} when I pay for {prom_down}/{prom_up}'

        time.sleep(5)
        try:
            sign_in = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div[2]/div/div/div/div/div/div/div[1]/a/div')
        except:
            sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()

        # base_window = self.driver.window_handles[0]
        # twitter_login_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(twitter_login_window)

        time.sleep(2.5)
        email = self.driver.find_element_by_css_selector('.r-30o5oe')
        email.send_keys(twit_email)

        time.sleep(2.5)
        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

        #time.sleep(2.5)
        #password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        #password.send_keys(twit_password)

        #time.sleep(2.5)
        #webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

        time.sleep(30)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(message)

        time.sleep(2.5)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div')
        tweet_button.click()

