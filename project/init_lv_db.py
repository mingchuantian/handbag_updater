
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(currentdir)


from project import db
from project.models import Item

def init_lv_db():
    
    Item.query.delete()
    print('lv all-rows-deleted')

    with open(currentdir + '/product-skus.txt', 'r') as skus:
        skus = skus.read().splitlines()
        for sku in skus:
            sku = sku.strip()
            item = Item(brand='lv', country='cn', sku=sku)
            db.session.add(item)
            db.session.commit()
    print('lv-cn created')

    with open(currentdir + '/product-skus.txt', 'r') as skus:
        skus = skus.read().splitlines()
        for sku in skus:
            sku = sku.strip()
            item = Item(brand='lv', country='us', sku=sku)
            db.session.add(item)
            db.session.commit()
    print('lv-us created')

    with open(currentdir + '/product-skus.txt', 'r') as skus:
        skus = skus.read().splitlines()
        for sku in skus:
            sku = sku.strip()
            item = Item(brand='lv', country='au', sku=sku)
            db.session.add(item)
            db.session.commit()
    print('lv-au created')