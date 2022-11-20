from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, ValidationError
from app.auth.models import User

def user_exists(form, field):
    user = User.query.filter_by(name=field.data).first()
    if user:
        raise ValidationError("User already exists")


class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), user_exists])
    password = PasswordField(validators=[DataRequired(), Length(min=6, message='Strong password')])
    confirm = PasswordField(validators=[DataRequired(), EqualTo('password', message='Password must match')])
    submit = SubmitField('register')


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')
