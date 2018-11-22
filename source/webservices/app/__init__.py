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

from app.application.controllers.customer import mod_customer as customer_module
from app.application.controllers.factory import mod_factory as factory_module

# Register blueprint(s)
app.register_blueprint(customer_module)
app.register_blueprint(factory_module)