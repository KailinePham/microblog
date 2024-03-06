'''
contains view functions that are mapped to their respective URLs;
passes data to the template for rendering 
'''

from flask import render_template
from app import app 
from app.forms import LoginForm

# decorators: modifies the function that it follows 
@app.route('/')     
@app.route('/index')

def index(): 
    '''
    a view function mapped to /index url to help render the posts 
    '''
    user = {'username': 'Miguel'}
    posts = [
        {'author': {'username': 'John'}, 'body': 'Beautiful day in Portland!'},
        {'author': {'username': 'Susan'}, 'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    '''
    view function mapped to /login URL to help render the sign-in page
    '''
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)