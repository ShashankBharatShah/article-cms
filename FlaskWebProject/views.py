"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for
from werkzeug.urls import url_parse
from config import Config
from FlaskWebProject import app, db
from FlaskWebProject.forms import LoginForm, PostForm
from flask_login import current_user, login_user, logout_user
from FlaskWebProject.models import User, Post
import msal
import uuid

imageSourceUrl = 'https://' + app.config['BLOB_ACCOUNT'] + '.blob.core.windows.net/' + app.config['BLOB_CONTAINER'] + '/'

@app.route('/')
@app.route('/home')
def home():
    # Temporary: avoid DB query to prevent SQL connection error
    posts = []
    return render_template(
        'index.html',
        title='Home Page',
        posts=posts
    )

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    # Temporary: disable DB write
    form = PostForm(request.form)
    return redirect(url_for('home'))

@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    # Temporary: disable DB edit
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Temporary login bypass (no DB authentication)
    form = LoginForm()

    if request.method == 'POST':
        return redirect(url_for('home'))

    session["state"] = str(uuid.uuid4())
    auth_url = ""
    return render_template(
        'login.html',
        title='Sign In',
        form=form,
        auth_url=auth_url
    )

@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('login'))

@app.route(Config.REDIRECT_PATH)
def authorized():
    return redirect(url_for('home'))

def _load_cache():
    cache = None
    return cache

def _save_cache(cache):
    pass

def _build_msal_app(cache=None, authority=None):
    return None

def _build_auth_url(authority=None, scopes=None, state=None):
    return ""
