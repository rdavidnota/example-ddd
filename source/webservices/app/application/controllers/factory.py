# Import flask dependencies
import json
from flask import Blueprint, request, Response
from app.application.factories.factory import Factory
import sys

factory_command = Factory.create_factory_command()

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_factory = Blueprint('factory', __name__, url_prefix='/factory')


# Set the route and accepted methods
@mod_factory.route('/save', methods=['POST'])
def save_factory():
    if request.method == 'POST':
        phone = request.values.get('phone')
        address = request.values.get('address')

        factory = 'save factory: {phone}, {address}'.format(phone=phone, address=address)

        print(factory)

        factory_command.create_factory(phone, address)
    return "OK"
