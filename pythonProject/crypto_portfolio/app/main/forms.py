from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class CoinAddForm(FlaskForm):
    symbol = StringField('symbol', validators=[DataRequired()])
    amount = FloatField('amount', validators=[DataRequired()])
    submit = SubmitField('Add')

class CoinUpdatePlus(FlaskForm):
    action = "Add: "
    amount = FloatField('amount', validators=[DataRequired()])
    submit_p = SubmitField('Submit')

class CoinUpdateMinus(FlaskForm):
    action = "Subtract: "
    amount = FloatField('amount', validators=[DataRequired()])
    submit_m = SubmitField('Submit')