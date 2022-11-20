from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), Length(min=6, message='Strong password')])
    confirm = PasswordField(validators=[DataRequired(), EqualTo('password', message='Password must match')])
    submit = SubmitField('register')


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')
