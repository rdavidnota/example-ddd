# Import flask and template operators
from flask import Flask, render_template

# Import a module / component using its blueprint handler variable
from app.application.controllers.customer import mod_customer as customer_module
from app.application.controllers.factory import mod_factory as factory_module

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Register blueprint(s)
app.register_blueprint(customer_module)
app.register_blueprint(factory_module)
