from selenium import webdriver
from time import sleep

class BadooBot():

    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver')


    def login(self):
        self.driver.get("https://badoo.com/")  # Open Badoo Website
        sleep(1.5)  # Wait 1.5 sec for load whole page

        log = self.driver.find_element_by_xpath("//*[@id='page']/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a") #find login with facebook button
        log.click() #click on this button

        window1 = self.driver.window_handles[0] # set defaut window because login by facebook button opened second window
        self.driver.switch_to_window(bot.driver.window_handles[1])  # switch to facebook login window

        sleep(1) # wait a second

        email = self.driver.find_element_by_xpath('//*[@id="email"]') # find email input 
        email.send_keys('your_fb_mail') # fill by yours email

        pw = self.driver.find_element_by_xpath('//*[@id="pass"]')  # find password input
        pw.send_keys('your_fb_password') # fill by yours password

        loginbt = self.driver.find_element_by_xpath('//*[@id="u_0_0"]') #find log in button 
        loginbt.click() # click login button

        self.driver.switch_to_window(window1) # back to badoo window


    def lubie(self):
    
            sleep(1)
            like = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')

            like.click()


    def message(self):
        match_popup = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[1]/div/section/div/div[2]/form/div/div[1]/div/input')
        match_popup.send_keys("your message")
        sleep(1.2)
        send_message = self.driver.find_element_by_xpath("/html/body/aside/section/div[1]/div/div[1]/div/section/div/div[2]/form/div/div[2]/div")
        send_message.click()

    def close_popup(self):
        popup3 = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div')
        popup3.click()


    def auto(self):
        while True:
            sleep(1)
            try:
                self.lubie()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.message()

            self.lubie()
