#/app/main/routes.py

from app.main import main
from app.main.models import Coin
from app.main.forms import CoinAddForm, CoinUpdatePlus, CoinUpdateMinus
from app import db
from app.main.utilities import get_coin_price
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
import os


@main.route('/')
@login_required
def home():
    return render_template('home.html',
                           coins=Coin.query.filter_by(owner_id=current_user.id).all(),
                           total=0,
                           user=current_user.name,
                           owner_id=current_user.id)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = CoinAddForm()

    if form.validate_on_submit():
        symbol = request.form['symbol'].lower()
        owner_id = current_user.id
        amount = request.form['amount']
        symbol_id = Coin.coin_identifier(request.form['symbol'])
        coin_exists = Coin.query.filter_by(symbol=symbol, owner_id=owner_id).first()
        if coin_exists:
            flash("Coin already exist. Please use details tab and update amount of a coin.")
            return redirect(url_for('main.home'))
        elif symbol_id == 429:
            flash("Coingecko api exausted. Please wait for couple of minutes. In free plan calls toward api are limited.")
            return redirect(url_for('main.home'))
        else:
            coin = Coin(symbol=symbol, amount=amount,
                        owner_id=owner_id, symbol_id=symbol_id)
            db.session.add(coin)
            db.session.commit()
            return redirect(url_for('main.home'))
    return render_template('coin_add.html', form=form)

@main.route('/delete/<symbol>', methods=['GET','POST'])
@login_required
def delete(symbol):
    if request.method in ['POST','GET']:
        coin = Coin.query.filter(Coin.symbol == symbol, Coin.owner_id == current_user.id).delete()
        db.session.commit()
        return redirect(url_for('main.home'))

@main.route('/details/<symbol>', methods=['GET', 'POST'])
@login_required
def coin_details(symbol):
    coin = Coin.query.filter_by(symbol=symbol, owner_id=current_user.id).first()
    form_plus = CoinUpdatePlus()
    form_minus = CoinUpdateMinus()

    if form_plus.submit_p.data and form_plus.validate_on_submit():
        print('tutaj')
        update_amount = coin[1] + float(request.form['amount'])
        db.session.query(Coin).filter(Coin.symbol == coin[0], Coin.owner_id == current_user.id).update({'amount': update_amount})
        db.session.commit()
        return redirect(url_for('main.home'))

    if form_minus.submit_m.data and form_minus.validate_on_submit():
        update_amount_minus = coin[1] - float(request.form['amount'])
        print(update_amount_minus)
        if update_amount_minus < 0:
            return 'error'
        else:
            db.session.query(Coin).filter(Coin.symbol == coin[0], Coin.owner_id == current_user.id).update({'amount': update_amount_minus})
            db.session.commit()
            return redirect(url_for('main.home'))
    return render_template('coin_details.html', coin=coin, form_plus=form_plus, form_minus=form_minus)
