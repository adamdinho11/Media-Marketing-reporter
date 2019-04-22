from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min = 4, max = 10)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 4, max = 12) ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password') ])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 4, max = 12) ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')