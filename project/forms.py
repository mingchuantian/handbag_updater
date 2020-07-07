from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):

    email_option = RadioField(
        'How would you like to be notified', 
        choices=[('product_only','Only notify me about specific product'),('all_products','I want notification of all products')],
        render_kw={'onchange': "radioButton()"})
    lv_options = SelectField(
        u'Choose your product',
        choices = [
            ( 'M44875','Pochette Metis (Monogram)  - M44875'), 
            ( 'M44876','Pochette Metis (Monogram Reverse Canvas)  - M44876'), 
            ( 'M44259','Marignan (Monogram)  - M44259'), 
            ( 'M44391','Dauphine (Monogram)  - M44391'), 
            ( 'M61276','Pochette Felicie (Monogram)  - M61276'), 
            ( 'N63106','Pochette Felicie (Azur)  - N63106'), 
            ('M63700','Valisette BB  - M63700'), 
            ( 'M44581','Valisette small  - M44581'), 
            ( 'M68623','Valisette vertical  - M68623'), 
            ( 'M43644','Bumbag (Monogram)  - M43644'), 
            ( 'M44860','Tambourin (Mongram)  - M44860'), 
            ( 'M52294','Boite Chapeau Souple (Monogram)  - M52294'), 
            ( 'M45149','Boite Chapeau Souple small (Monogram)  - M45149'), 
            ( 'M44699','Boite Chapeau Souple Mini (Monogram)  - M44699'), 
            ( 'M61252','Nano Speedy  - M61252'), 
            ( 'M40718','Favorite MM (Monogram)  - M40718'), 
            ( 'N41129','Favorite MM (Ebene)  - N41129'), 
            ( 'N41275','Favorite MM (Azur)  - N41275'), 
            ( 'M40817','Noe BB (Monogram)  - M40817'), 
            ( 'N41220','Noe BB (Azur)  - N41220' ), 
            ( 'M42224','Noe (Monogram)  - M42224'), 
            ( 'N42222','Noe (Azur)  - N42222'), 
            ( 'M40818','Noe NM  - M40818'), 
            ( 'M40712','Pochette Accessories (Monogram)  - M40712'), 
            ( 'N41207','Pochette Accessories (Azur)  - N41207'), 
            ( 'M44840','Multi Pochette Accessories (Rose Clair)  - M44840'), 
            ( 'Others','Others (Please specify SKU)')] 
    )
    hermes_options = SelectField(
        u'Choose your product',
        choices = [('Hermes bb', 'hermes bb'), ('Alma bb', 'Alma bb'), 
        ('Others(Please specify)', 'Others')] 
    )
    other_options = StringField('Other options')
    region = SelectField(
        u'Pick your online store location',
        choices = [('cn', 'China mainland'), ('us', 'United States'), 
        ('au', 'Australia')]
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

class addSKUForm(FlaskForm):
    brand = SelectField(u'Choose brand', choices = [('lv', 'lv')])   
    country = SelectField(u'Select country', choices = [('cn', 'cn'), ('au', 'au'), ('us', 'us')])  
    SKU = StringField('SKU', validators=[DataRequired()])
    submit = SubmitField('Submit')
