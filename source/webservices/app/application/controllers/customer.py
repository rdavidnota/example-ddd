# Import flask dependencies
import json
from flask import Blueprint, request, Response
from app.application.factories.factory import Factory

customer_command = Factory.create_customer_command()

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_customer = Blueprint('customer', __name__, url_prefix='/customer')


# Set the route and accepted methods
@mod_customer.route('/save', methods=['POST'])
def SaveCustomer():
    if request.method == 'POST':
        name = request.values.get('name')
        customer_command.save_customer(name)
    return "OK"


# Set the route and accepted methods
@mod_customer.route('/list', methods=['GET'])
def ListCustomer():
    customers = []
    if request.method == 'GET':
        customers = customer_command.list_customer()

    response = json.dumps([cus.toJSON() for cus in customers]),

    return Response(response=response, status=202, mimetype='application/json')
