# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

from sqlalchemy import create_engine
from app.persistence.entities.models import Base



# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
# from app.mod_auth.controllers import mod_auth as auth_module

from app.hello.controllers import mod_hello as hello_module

# Register blueprint(s)
app.register_blueprint(hello_module)
