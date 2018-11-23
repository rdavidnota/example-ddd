from django.shortcuts import render
from customer.apirest.customer import list_customers


# Create your views here.

def get_customers(request):
    customers = list_customers()
    return render(request, 'customer/list_customers.html',
                  {'customers': customers})
