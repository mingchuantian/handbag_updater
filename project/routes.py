import csv
from project import app, bcrypt, db, mail, Message
from flask import render_template, url_for, flash, redirect
from project.models import User, Item, subscribes
from project.forms import RegistrationForm, UserRegistration, LoginForm, addSKUForm
from project.init_lv_db import init_lv_db
from project.crawler import website_handler
from flask_login import login_user, current_user, logout_user, login_required




@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.lv_options.data)
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user, remember=True)
            if form.lv_options.data == 'Others':
                #register from another field
                pass
            else:
                #add current user & product combination to the relation table
                item = Item.query.filter_by(sku=form.lv_options.data, country=form.region.data).first()
                item.subscribed_users.append(current_user)
                db.session.commit()
                #send email
                msg = Message("Welcome back, successfully subscribed", sender=("Updater24","mingchuantian1@gmail.com"), recipients=[form.email.data])
                mail.send(msg)
        else:
            if form.lv_options.data == 'Others':
                #register from another field
                pass
            else:
                user = User(email=form.email.data)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                item = Item.query.filter_by(sku=form.lv_options.data, country=form.region.data).first()
                item.subscribed_users.append(current_user)
                db.session.commit()
                #send email
                msg = Message("Welcome! Successfully subscribed", sender=("Updater24","mingchuantian1@gmail.com"), recipients=[form.email.data])
                mail.send(msg)
        return 'subscribed successfully!'
    print(form.errors)
    return render_template('index.html', form=form)



@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = UserRegistration()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash(f'Account exists for {form.username.data}!', 'danger')
        else:   
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Account_created for {form.username.data}!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                #can take two arguments, second is for remember
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))
            else:
                flash('Login unsuccessful!', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
def account():
    return 'account'


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = addSKUForm()
    if form.validate_on_submit():
        item = Item(brand=form.brand.data, country=form.country.data, sku=form.SKU.data)
        db.session.add(item)
        db.session.commit()
        flash('Item added to database', 'success')
    return render_template('admin.html', form=form)


@app.route('/init_db', methods=['GET', 'POST'])
def init_db():
    init_lv_db()
    print('initialized')
    return redirect(url_for('admin'))

@app.route('/websites_scan', methods=['GET', 'POST'])
def websites_scan():
    countries = ['cn', 'us', 'au']
    for country in countries:
        items = Item.query.filter_by(country=country)
        print(f'Now performing scan for {country} skus!')
        for item in items:
            was_available = item.is_available
            crawler = website_handler()
            crawler.open(item.sku)
            try:
                is_now_available = crawler.get_status()
            except:
                is_now_available = False
                crawler.close()
                flash('there was something wrong when performing the search')
            
            if is_now_available:
                print(f'{item.sku} item found')
                users = item.subscribed_users
                for user in users:
                    print(f'{user.email} now send email')
                    try:
                        email = user.email
                        msg = Message("Item now available for purchase!", sender=("Updater24","mingchuantian1@gmail.com"), recipients=[email])
                        mail.send(msg)  
                    except:
                        print('something wrong')   
                    #this is not working properly    
                    item.subscribed_users.remove(user)
                    print('user stauts deleted')
                    db.session.commit()
                
            crawler.close()
    return redirect(url_for('admin'))

#test script

'''
user1 = User(email='1120509786@qq.com')
user2 = User(email='mingchuantian1@gmail.com')
item1 = Item(brand='lv', country='cn', sku='M44875')
item2 = Item(brand='lv', country='cn', sku='M44876')
db.session.add(user1, user2, item1, item2)
'''

'''
item1.subscribed_users.append(user1)
item2.subscribed_users.append(user2)
item2.subscribed_users.append(user1)
db.session.commit()
'''