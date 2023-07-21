from flask import render_template, flash, redirect
from app import app #connects with instance of app in the __init__file of the app folder
from app.forms import LoginForm, RegisterForm


@app.route('/') #decorator that wraps a function and points to a specifc url. It says apply this function when going to this endpoint (URL).
def home(): #viewer function (i.e., determines what will be viewed at the given url endpoint)
    author_posts = {
        'author': {
            'Mike': ['Be on the lookout for some banjo-picking, crime-fighting grandmas heading your way!'],
            'Brandon': ["I can't wait! We need more grandmas out there repping the seasoned crime fighters"]
        },
        'students': {student:[f'Yay! More books from Mike! We loved Raymond and Graham!'] for student in ['Mark', 'Kimmy', 'Steve', "Karin"]}
    }
    return render_template('index.jinja', authors=author_posts['author'], students=author_posts['students'], title='Homepage')



@app.route('/signin', methods=["GET", "POST"])
def sign_in():
    login_form = LoginForm() #creating an instance of the imported class
    if login_form.validate_on_submit():
        flash(f'{login_form.email.data} has logged in!', category='success')
        return redirect('/')
    return render_template('signin.jinja', title='Sign In', form = login_form)


@app.route('/register', methods=["GET", "POST"])
def sign_up():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        first_name = register_form.first_name.data
        username = register_form.username.data
        flash(f'{first_name if first_name else username} has registered!', category='success')
        return redirect('/')
    return render_template('register.jinja', title="Sign Up", form = register_form)


@app.route('/collections_books')
def collections_books():
    return render_template('collections_books.jinja', title="Books")