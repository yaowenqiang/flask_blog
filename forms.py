from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataReqiured,Length, Email, EqualTo

class  RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataReqiured(),Length(min=2, max=20)])

    email = StringField('Email', validators=[DataReqiured(), Email()])
    password = PasswordField('Password', validators=[DataReqiured()])
    ConfirmPassword = PasswordField('Confirm Password', validators=[DataReqiured(), EqualTo('password')])
    submit = SubmitField('Sign up')


class  LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataReqiured(), Email()])
    password = PasswordField('Password', validators=[DataReqiured()])
    remember = BooleanField('Remember Me', validators=[DataReqiured()])
    submit = SubmitField('Login')


