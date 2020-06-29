import csv
from project import app
from flask import render_template
from project.forms import RegistrationForm


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