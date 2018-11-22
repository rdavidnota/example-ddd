# Import flask dependencies
from flask import Blueprint
from app.persistence.message import hello_world
from app.persistence.customer import SaveCustomer

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_hello = Blueprint('hello', __name__, url_prefix='/hello')


# Set the route and accepted methods
@mod_hello.route('/hello_world/', methods=['POST'])
def HelloWorld():
    SaveCustomer()
    return hello_world()
