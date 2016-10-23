from django.shortcuts import render

def customer(request):
        return render(request, 'presta_do/customer.html', {})