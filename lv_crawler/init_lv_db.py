#import from parent directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from project import db
from project.models import Item

db.drop_all()
db.create_all()

with open('product-skus.txt', 'r') as skus:
    for sku in skus:
        item = Item(brand='lv', country='cn', sku=sku)
        db.session.add(item)
        db.session.commit()

with open('product-skus.txt', 'r') as skus:
    for sku in skus:
        item = Item(brand='lv', country='us', sku=sku)
        db.session.add(item)
        db.session.commit()

with open('product-skus.txt', 'r') as skus:
    for sku in skus:
        item = Item(brand='lv', country='au', sku=sku)
        db.session.add(item)
        db.session.commit()