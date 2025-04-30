from flask import Blueprint, render_template, request

#from models import user, Post

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/blog')
def blog():
    return render_template('blog.html')