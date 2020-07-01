from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    brand = SelectField(
        u'Select your brand',
        choices = [('LV', 'LV'), ('Hermes', 'Hermes'), 
        ('LEGO', 'LEGO')], 
        render_kw={'onchange': "myFunction()"}
    )
    email_option = RadioField(
        'How would you like to be notified', 
        choices=[('product_only','Only notify me about specific product'),('all_products','I want notification of all products')],
        render_kw={'onchange': "radioButton()"})
    lv_options = SelectField(
        u'Choose your product',
        choices = [('Monogram bb', 'Monogram bb'), ('Alma bb', 'Alma bb'), 
        ('Others(Please specify)', 'Others')] 
    )
    hermes_options = SelectField(
        u'Choose your product',
        choices = [('Hermes bb', 'hermes bb'), ('Alma bb', 'Alma bb'), 
        ('Others(Please specify)', 'Others')] 
    )
    other_options = StringField('Other options', validators=[DataRequired()])
    region = SelectField(
        u'Pick your online store location',
        choices = [('China mainland', 'China mainland'), ('United States', 'United States'), 
        ('United Kingdom', 'United Kingdom')]
    )
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Sign up')

class UserRegistration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20, message='Length can only between 2 and 20')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
