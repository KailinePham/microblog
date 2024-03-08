'''
contains view functions that are mapped to their respective URLs;
passes data to the template for rendering 
'''

from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST']) 
# methods arg tells flask that this view func accepts GET and POST requests 
# default tells flask that the view function only accepts GET requests 
#   POST requests --> used when the browser submits form data to the server 
def login():
    '''
    view function mapped to /login URL to help render the sign-in page
    '''
    form = LoginForm()
    # returns False when the browser sends a POST request (user hit submit)
    if form.validate_on_submit(): # does all the form processing work
        # stores msg to be shown later when rendered 
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remeber_me.data)) 
        return redirect(url_for('index')) # navigate to index page 
    return render_template('login.html', title='Sign In', form=form)