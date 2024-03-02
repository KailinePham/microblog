from flask import render_template
from app import app 

# decorators: modifies the function that it follows 
@app.route('/')     
@app.route('/index')

def index(): 
    '''
    a view function that returns a greeting as a string 
    '''
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)
