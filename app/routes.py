from app import app 

# decorators: modifies the function that it follows 
@app.route('/')     
@app.route('/index')

def index(): 
    '''
    a view function that returns a greeting as a string 
    '''
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''