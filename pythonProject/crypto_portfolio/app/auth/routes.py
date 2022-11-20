from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint, session
from app.auth.models import User
from flask_login import LoginManager
from flask_login import login_required, logout_user, login_user, current_user
from sqlalchemy.sql import func

from app.auth.forms import SignupForm, LoginForm
from app.auth import authentication as at
from app.main import main
from app import login_manager, db


@at.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('signup.html', title="Create account", form=form)

@at.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        flash('Invalid user/pass')
        return redirect(url_for('authentication.login'))
    return render_template('login.html', form=form)

@at.route('/logout')
def logout():
    logout_user()
    db.session.close()
    return redirect(url_for('main.home'))