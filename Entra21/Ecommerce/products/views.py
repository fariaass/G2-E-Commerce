from django.shortcuts import render
import requests

def product(request):
    """
    This function takes the data from the api, extracts in json format and return rendering a template with the json data
    """
    data = requests.get('http://127.0.0.1:8000/api/products')
    data = data.json()
    return render(request, 'EM ABERTO', {'data':data})