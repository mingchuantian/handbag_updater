import os, time, csv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from flask import Flask
from flask_mail import Mail, Message

from selenium.webdriver.chrome.options import Options

#option for headless
'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
'''


app = Flask(__name__)
ctx = app.app_context()
ctx.push()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'mingchuantian1@gmail.com'
app.config['MAIL_PASSWORD'] = 'tianmingchuan123'

mail = Mail(app)

class AutoCrawler:

    def __init__(self, link):
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.link = link
        self.driver = webdriver.Chrome(executable_path=os.path.join(self.basedir,'chromedriver'))

    def run(self):
        self.driver.get(self.link)
    
    def close(self):
        self.driver.close()
    
    def get_status(self):
        #try:
        button = self.driver.find_element_by_id('addToCartFormHolder')
        if button.get_attribute('class') == 'hide':
            print('Unavailable, now try next product...')
            return
        else:
            print('product available')
            recipients = self.get_recipients()
            try:
                with mail.connect() as conn:
                    for recipient in recipients:
                        message = self.link
                        subject = '你的商品已经可以购买了'
                        msg = Message(recipients=recipient, body=message, subject=subject, sender='mingchuantian1@gmail.com')
                        conn.send(msg)
            except:
                pass
        #except:
        #    print('exception')

    def get_recipients(self):
        try:
            with open('data.csv', newline='') as csvfile:
                members = csv.reader(csvfile, delimiter=',')
                print(members)
                recipients = []
                for member in members:
                    print(member)
                    recipients.append(member)
            return recipients
        except:
            pass

if __name__=='__main__':
    while True:
        with open('websites.txt', 'r') as websites:
            for website in websites:
                crawler = AutoCrawler(website)
                crawler.run()
                crawler.get_status()
                crawler.close()
    ctx.pop()