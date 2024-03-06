import os

class Config: 
    # secret key is the most important part in most flask apps
    #   - can be used as a cryptographic key to generate 
    #     signatures or tokens
    #   - Flask-WTF extension uses it to protect against CSRF attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    