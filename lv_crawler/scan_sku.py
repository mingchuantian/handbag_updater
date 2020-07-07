import os, sys, inspect, time, csv
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from project.models import Item


# For mail delivery
'''
from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)
ctx = app.app_context()
ctx.push()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'mingchuantian1@gmail.com'
app.config['MAIL_PASSWORD'] = 'tianmingchuan123'

mail = Mail(app)
'''

class sku_scanner():

    def __init__(self):
        self.link = 'https://www.louisvuitton.cn/zhs-cn/search/'
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
    
    def get_status(self):
        pass

    def open(self, sku):
        self.driver.get(self.link + sku)

    def close(self):
        self.driver.close()


class email_sender():

    def __init__(self):
        pass

    def send_email(self):
        with mail.connect() as conn:
            for recipient in recipients:
                message = self.link
                subject = '你的商品已经可以购买了'
                msg = Message(recipients=recipient, body=message, subject=subject, sender='mingchuantian1@gmail.com')
                conn.send(msg)


all_skus = Item.query.filter_by(country='cn')

for sku in all_skus:
    scanner = sku_scanner()
    scanner.open(sku.sku)
    time.sleep(2)
    scanner.close()

'''
with open('product-skus.txt', 'r') as skus:
    for sku in skus:
        scanner = sku_scanner()
        scanner.open(sku)
        time.sleep(2)
        scanner.close()
'''