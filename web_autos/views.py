from django.shortcuts import render
from .models import Brand, Car, Owner

def index(request):
    return render(request, 'web_autos/index.html')

def add_brand(request):
    # Lógica para agregar una nueva marca
    return render(request, 'web_autos/add_brand.html')

def add_car(request):
    # Lógica para agregar un nuevo coche
    return render(request, 'web_autos/add_car.html')

def add_owner(request):
    # Lógica para agregar un nuevo propietario
    return render(request, 'web_autos/add_owner.html')

def search(request):
    # Lógica para buscar en la base de datos
    return render(request, 'web_autos/search.html')
