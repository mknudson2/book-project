from flask import render_template
from . import bp as main



@main.route('/') #decorator that wraps a function and points to a specifc url. It says apply this function when going to this endpoint (URL).
def home(): #viewer function (i.e., determines what will be viewed at the given url endpoint)
    author_posts = {
        'author': {
            'Haraldur': ['Við erum mjög glöð að bjóða alla ny bók um ritsagn Íslands!'],
            'Bragi': ["Frábært! Það verða allir þakksöm efitr."]
        },
        'students': {student:[f'Jæja! Bækur fyrir alla!'] for student in ['Svanhildur', 'Regin', 'Snæbjörn', "Helgi"]}
    }
    return render_template('index.jinja', authors=author_posts['author'], students=author_posts['students'], title='Homepage')




@main.route('/collections_books')
def collections_books():
    return render_template('collections_books.jinja', title="Books")