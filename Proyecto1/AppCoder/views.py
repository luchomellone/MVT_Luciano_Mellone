from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from datetime import datetime

def fam(request, nombre, apellido, edad, nacimiento):

    familiar = Familia(nombre = nombre, apellido = apellido, edad = edad)
    fecha = datetime.strptime(nacimiento, "%d-%m-%Y").date()
    
    familiar.fecha = fecha
    
    familiar.save()

    return HttpResponse(
        f"""<p>Nombre: {familiar.nombre} {familiar.apellido} - agregado correctamente"""
    )

def lista_de_familiares(request):
    
    list = Familia.objects.all()
    
    return render(request, 'templates.html', {'lista_de_familiares':list})