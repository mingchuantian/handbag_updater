
from selenium import webdriver
from project.models import Item


class website_handler():

    def __init__(self):
        self.link = 'https://www.louisvuitton.cn/zhs-cn/search/'
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
    
    def get_status(self):
        #time.sleep(2)
        button = self.driver.find_element_by_id('addToCartFormHolder')
        if button.get_attribute('class') == 'hide':
            print('Unavailable, now try next product...')
            return False
        else:
            print('product available')
            return True
            '''
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
            '''

    def open(self, sku):
        self.driver.get(self.link + sku)

    def close(self):
        self.driver.close()