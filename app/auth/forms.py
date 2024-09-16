"""  This module contains the forms for the authentication blueprint. """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.validators import NumberRange

class LoginForm(FlaskForm):
    """Form for users to log in."""
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    """Form for users to create a new account."""
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6), EqualTo('password', message='password doesn\'t match')])
    submit = SubmitField('Register')

class ChildProfileForm(FlaskForm):
    """ Form for parents to create a child profile """
    username = StringField('Child Username', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Create Profile')
