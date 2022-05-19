from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField,TextAreaField, IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
  username =  StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  age = IntegerField('Age', validators=[DataRequired(),])
  bloodgroup = StringField('Blood Group', validators=[DataRequired(),])
  conditions = TextAreaField('Pre-existing conditions', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Re-Enter Password', validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Submit')




 


