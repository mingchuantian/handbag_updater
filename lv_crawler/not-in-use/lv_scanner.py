import os, time, csv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class lv_scanner():

    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Chrome(executable_path='../chromedriver')

    def scroll_buttom(self):
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_urls(self):
        product_container = self.driver.find_element_by_class_name("lv-paginated-list")
        list_container = product_container.find_element_by_class_name("lv-list")
        product_list = list_container.find_elements_by_tag_name("li")
        for product in product_list:
            a_tag = product.find_element_by_tag_name('a')
            link = a_tag.get_attribute('href')
            print(link)

    def run(self):
        self.driver.get(self.link)
    
    def close(self):
        self.driver.close()




with open('websites.txt', 'r') as websites:
    for website in websites:
        hunter = lv_scanner(website)
        hunter.run()
        hunter.scroll_buttom()
        hunter.driver.implicitly_wait(5)
        hunter.get_urls()
