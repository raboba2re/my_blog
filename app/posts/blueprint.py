from flask import Blueprint, render_template
from models import Post

posts = Blueprint('Posts', __name__, template_folder='templates')

@posts.route('/')
def posts_list():
    posts = Post.query.all()
    return render_template('posts/post.html', posts = posts)


@posts.route('/<slug>')
def post_details(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post = post) 