from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class signupForm(FlaskForm):
    First_Name = StringField('First Name', validators = [DataRequired("*Name Required")])
    Last_Name = StringField('Last Name', validators = [DataRequired("*Name Required")])
    Email = StringField('Email', validators = [DataRequired("*Email Required"), Email("*Invalid Email Address")])
    Password = PasswordField('Password', validators = [DataRequired("*Password Required"), Length(min=5, message="Password must be at least 5 characters")])
    submit = SubmitField('Sign Up')

class loginForm(FlaskForm):
    Email = StringField('Email', validators = [DataRequired("*Email Required"), Email("*Invalid Email Address")])
    Password = PasswordField('Password', validators = [DataRequired("*Password Required")])
    submit = SubmitField("Log In")
