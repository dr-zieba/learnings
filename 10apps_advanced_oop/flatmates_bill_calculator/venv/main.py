from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

app = Flask(__name__)

class Bill(object):
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate(object):
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay(self, bill, flatmate2):
        weight = int(self.days_in_house) / (int(self.days_in_house) + int(flatmate2.days_in_house))
        to_pay = bill.amount * weight
        return  to_pay

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)

class ResultPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)
        amount = bill_form.amount.data
        period = bill_form.period.data
        flatmate1 = bill_form.flatmate1.data
        day1 = bill_form.days1.data
        flatmate2 = bill_form.flatmate2.data
        day2 = bill_form.days2.data

        bill = Bill(float(amount), period)

        flat1 = Flatmate(flatmate1, day1)
        flat2 = Flatmate(flatmate2, day2)

        #return f"({flat1.name} pays: {flat1.pay(bill, flat2)} {flat2.name} pays: {flat2.pay(bill, flat1)})"
        return render_template('result.html',
                               flatmate1 = flat1.name,
                               flatmate2 = flat2.name,
                               flat1pay = flat1.pay(bill, flat2),
                               flat2pay = flat2.pay(bill, flat1))

class BillForm(Form):
    amount = StringField("Amount: ")
    period = StringField("Period: ")

    flatmate1 = StringField("Name: ")
    days1 = StringField("Days in the house: ")

    flatmate2 = StringField("Name: ")
    days2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_page', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))

app.run()