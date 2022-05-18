from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField,TextAreaField, IntegerField,SelectField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
# from  zebus.models import User


class RegistrationForm(FlaskForm):
  username =  StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  age = IntegerField('Age', validators=[DataRequired(),])
  blood_group = SelectField('Blood Group', validators=[DataRequired(),])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Re-Enter Password', validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Submit')