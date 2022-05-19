from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField, IntegerField,SelectField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
  username =  StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  age = IntegerField('Age', validators=[DataRequired(),])
  bloodgroup = SelectField('Blood Group', validators=[DataRequired(),])
  conditions = TextAreaField('existing_conditions', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Re-Enter Password', validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Submit')