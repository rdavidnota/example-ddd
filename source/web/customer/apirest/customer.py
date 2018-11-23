import requests

def list_customers():
    response = requests.get('http://localhost:8080/customer/list')
    customers = response.json()

    return customers
