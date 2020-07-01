import os, time, csv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class sku_scanner():

    def __init__(self):
        self.link = 'https://www.louisvuitton.cn/zhs-cn/search/'
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
    
    def get_product(self, sku):
        search_input = self.driver.find_element_by_id('searchHeaderInput')
        search_input.send_keys(sku)
        search_input.send_keys(Keys.ENTER)


    def open(self, sku):
        self.driver.get(self.link + sku)

    def close(self):
        self.driver.close()


with open('product-skus.txt', 'r') as skus:
    for sku in skus:
        scanner = sku_scanner()
        scanner.open(sku)
        time.sleep(2)
        scanner.close()