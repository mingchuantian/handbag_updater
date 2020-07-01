import csv
from project import app, bcrypt, db
from flask import render_template, url_for, flash, redirect
from project.models import User
from project.forms import RegistrationForm, UserRegistration, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        with open('data.csv', 'a', newline='') as n:
            useremail = form.email.data
            print(useremail)
            writer = csv.writer(n)
            writer.writerow([useremail])
        return 'Successfully registered!'

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