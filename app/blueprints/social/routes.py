from flask import render_template, redirect, flash, url_for, g
from flask_login import current_user, login_required
from app import app
from app.forms import CollectionForm, PostForm, UserSearchForm
from app.models import Collection, Post, User
from . import bp

@app.before_request
def before_request():
    g.search_form = UserSearchForm()
    g.post_form = PostForm()
    g.collection_form = CollectionForm()

@bp.post('/post')
def post():
    if g.post_form.validate_on_submit():
        post = Post(body = g.post_form.body.data, user_id = current_user.user_id)
        post.commit()
        flash('Posted', category = 'success')
    return redirect(url_for('social.profile', username = current_user.username))

@bp.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username = username).first()
    if user:
        posts = user.posts
        collections = user.collection
        # print(collections)
        # print(collections[0].book_title)
        return render_template('profile.jinja', username = username, posts = posts, collections = collections)
    else:
        flash(f'User: {username} is not a valid user',category='alert')
        return redirect(url_for('main.home'))
    
@bp.post('/user-search')
def user_search():
    return redirect(url_for('social.profile', username = g.search_form.username.data))
    
@bp.post('/add-to-collection')
def collection_add():
    if g.collection_form:
        add_to = Collection(
            book_title = g.collection_form.book_title.data, 
            author = g.collection_form.author.data, 
            year_published = g.collection_form.year_published.data, 
            language = g.collection_form.language.data, 
            description = g.collection_form.description.data, 
            type = g.collection_form.type.data, 
            user_id = current_user.user_id
            )
        add_to.commit()
        flash('Added to Collection', category = 'success')
    return redirect(url_for('main.home', username=current_user.username))
