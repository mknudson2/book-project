from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from . import bp as api
from app.models import Post, User

@api.post('/publish-post')
@jwt_required() #Ensures that you can only access this once logged in
def publish_post():
    body = request.json.get('body')
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    try:
        p = Post(body=body, user_id = user.user_id)
        p.commit()
    except:
        jsonify(message='Error, please try again.'), 404
    return jsonify({
        'message': 'Success! Post published.',
        'logged_in_as': username
    }), 200

@api.get('/user-posts/<username>')
@jwt_required()
def get_user_posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Invalid username'}), 400
    user_posts = user.posts
    return jsonify({
        'message': 'success',
        'posts': [{
            'body': post.body,
            'timestamp': post.timestamp
        } for post in user_posts ]
        
    })

@api.get('/user-collection/<username>')
@jwt_required()
def get_user_collection(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Invalid username'}), 400
    user_collection = user.collection
    return jsonify({
        'message': 'success',
        'collections': [{
            'book_title': collection.book_title,
            'author': collection.author,
            'year_published': collection.year_published,
            'language': collection.language,
            'description': collection.description,
            'type': collection.type
        } for collection in user_collection]
    })

@api.delete('/delete-post/<post_id>')
@jwt_required()
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify(message='Invalid post id.'), 400
    print(post.author)
    if post.author.username != get_jwt_identity():
        return jsonify(message='You cannot delete this post.'), 400
    post.delete()
    return jsonify(message='Post deleted.')

@api.get('/user-profile/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(user=user.to_dict)
    return jsonify(message='Invalid username.'), 404