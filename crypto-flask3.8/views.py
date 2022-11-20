from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
from display import display
from models import Coin, db, User
from price import check
from flask_login import LoginManager
from forms import SignupForm, LoginForm
from flask_login import login_required, logout_user, login_user, current_user
from sqlalchemy.sql import func

views = Blueprint('views', __name__, template_folder='templates', static_folder='static')
login_manager = LoginManager()

@views.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404

@views.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.show'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('views.show'))
        flash('Invalid user/pass')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(name=form.name.data).first()
        if existing_user is None:
            user = User(name=form.name.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('views.show'))
    flash('User already exists')
    return render_template('signup.html', title="Create account", form=form)

@views.route('/logout')
def logout():
    logout_user()
    db.session.close()
    return redirect(url_for('views.login'))

@views.route('/show')
@login_required
def show():
    return render_template('coins_index.html',
                           symbols=Coin.query.filter_by(owner_id=current_user.id),
                           check=check,
                           total=0,
                           user=current_user.name)

@views.route('/show/<symbol>')
@login_required
def show_details(symbol):
    symbol = Coin.query.filter_by(symbol=symbol).one()
    return render_template('coin_show.html', symbol=symbol)

@views.route('/show/update/<symbol>', methods=['GET', 'POST'])
@login_required
def update(symbol):
    if request.method == 'POST':
        if not request.form['amount']:
            return "error"
        else:
            amount_to_add = request.form['amount']
            current_amount = db.session.query(Coin.amount).filter_by(symbol=symbol).first()
            b = [float(x) for x in current_amount]
            amount = float(amount_to_add) + float(b[0])
            condition = db.session.query(Coin).filter(Coin.symbol == symbol).update({'amount': amount})
            db.session.commit()
            return redirect(url_for('views.show'))
    return render_template('coins_update.html', symbol=Coin.query.filter_by(symbol=symbol).one())

@views.route('/show/minus/<symbol>', methods=['GET', 'POST'])
@login_required
def minus(symbol):
    if request.method == 'POST':
        if not request.form['amount']:
            return "error"
        else:
            amount_to_minus = request.form['amount']
            current_amount = db.session.query(Coin.amount).filter(Coin.symbol==symbol, Coin.owner_id == current_user.id ).first()
            b = [float(x) for x in current_amount]
            amount = float(b[0]) - float(amount_to_minus)

            if amount <= 0:
                flash("Amount lower then 0")
                return render_template('coins_minus.html', symbol=Coin.query.filter(Coin.symbol==symbol, Coin.owner_id == current_user.id).one())
            else:
                db.session.query(Coin).filter(Coin.symbol == symbol, Coin.owner_id == current_user.id).update({'amount': amount})
                db.session.commit()
                return redirect(url_for('views.show'))
    return render_template('coins_minus.html', symbol=Coin.query.filter_by(symbol=symbol).one())

@views.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        if not request.form['symbol'] or not request.form['amount']:
            return "error"
        else:
            coin = Coin(symbol=request.form['symbol'], amount=request.form['amount'], owner_id=current_user.id)
            db.session.add(coin)
            db.session.commit()
            return redirect(url_for('views.show'))
    return render_template('coins_add.html')

@views.route('/delete/<symbol>', methods=['GET','POST'])
@login_required
def delete(symbol):
    if request.method in ['POST','GET']:
        coin = Coin.query.filter(Coin.symbol == symbol, Coin.owner_id == current_user.id).delete()
        db.session.commit()
        return redirect(url_for('views.show'))

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    flash("Login!!, 401")
    return redirect(url_for('views.login'))