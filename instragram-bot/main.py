from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(4)


InstaBot('acharyyaswastik', '41arpan@#great')
