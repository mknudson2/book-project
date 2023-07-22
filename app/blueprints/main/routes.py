from flask import render_template
from . import bp as main



@main.route('/') #decorator that wraps a function and points to a specifc url. It says apply this function when going to this endpoint (URL).
def home(): #viewer function (i.e., determines what will be viewed at the given url endpoint)
    author_posts = {
        'author': {
            'Mike': ['Be on the lookout for some banjo-picking, crime-fighting grandmas heading your way!'],
            'Brandon': ["I can't wait! We need more grandmas out there repping the seasoned crime fighters"]
        },
        'students': {student:[f'Yay! More books from Mike! We loved Raymond and Graham!'] for student in ['Mark', 'Kimmy', 'Steve', "Karin"]}
    }
    return render_template('index.jinja', authors=author_posts['author'], students=author_posts['students'], title='Homepage')




@main.route('/collections_books')
def collections_books():
    return render_template('collections_books.jinja', title="Books")