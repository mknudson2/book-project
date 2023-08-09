from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, current_user, login_required

from . import bp as auth
from app.forms import LoginForm, RegisterForm
from app.models import User



@auth.route('/signin', methods=["GET", "POST"])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    login_form = LoginForm() #creating an instance of the imported class
    if login_form.validate_on_submit():
        email = login_form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(login_form.password.data):
            login_user(user)
            flash(f'{login_form.email.data} has logged in!', category='success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid user data. Please try again.', category='warning')
    return render_template('signin.jinja', title='Sign In', form = login_form ) #How we then access our form on the page/template


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.sign_in'))

@auth.route('/register', methods=["GET", "POST"])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_info = { 
        'first_name' : register_form.first_name.data,
        'last_name' : register_form.last_name.data,
        'username' : register_form.username.data,
        'email' : register_form.email.data
        }
        try:
            user = User()
            user.from_dict(user_info)
            user.hash_password(register_form.password.data)
            user.commit()
            flash(f'{user.first_name if user.first_name else user.username} has registered!', category='success')
            login_user(user)
            return redirect(url_for('main.home'))
        except:
            flash('Username or email is already taken. Please try again', category="warning")
    return render_template('register.jinja', title="Sign Up", form = register_form)