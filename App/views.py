from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from App.forms import sedanform
from App.forms import coupeform
from App.forms import suvform
from App.models import Sedan
from App.models import Coupe
from App.models import Suv

# Create your views here.

def inicio(request):
    return render(request, "App/inicio.html")
def ver_sedan(request):
    return render(request, "App/ver_sedan.html")
def ver_coupe(request,):
    return render(request, "App/ver_coupe.html")
def ver_suv(request):
    return render(request, "App/ver_suv.html")
def sedanformulario(request):
    if request.method== "POST":
        formulario1= sedanform(request.POST)
        if formulario1.is_valid():
            info= formulario1.cleaned_data
            sedan= Sedan(marca=info["marca"], modelo=info["modelo"], fechacompra=info["fechacompra"])
            sedan.save()
            return render(request, "App/inicio.html")
    else:
        formulario1= sedanform()

    return render(request, "App/sedanform.html", {"form1":formulario1})
def busquedamodelo(request):
    return render(request, "App/inicio.html")
def Resultado(request):
    if request.GET["modelo"]:
        modelo= request.GET["modelo"]
        sedan= Sedan.objects.filter(modelo__icontains=modelo)
        return render(request, "App/inicio.html", {"modelo": modelo})
    return HttpResponse(f"Estas buscando el modelo: {request.GET['modelo']}")
def coupeformulario(request):
    if request.method== "POST":
        formulario2= coupeform(request.POST)
        if formulario2.is_valid():
            info2= formulario2.cleaned_data
            coupe= Coupe(marca=info2["marca2"], modelo=info2["modelo2"], fechacompra=info2["fechacompra2"])
            coupe.save()
            return render(request, "App/inicio.html")
    else:
        formulario2= coupeform()

    return render(request, "App/coupeform.html", {"form2":formulario2})
def suvformulario(request):
    if request.method== "POST":
        formulario3= suvform(request.POST)
        if formulario3.is_valid():
            info3= formulario3.cleaned_data
            suv= Suv(marca=info3["marca3"], modelo=info3["modelo3"], fechacompra=info3["fechacompra3"])
            suv.save()
            return render(request, "App/inicio.html")
    else:
        formulario3= suvform()

    return render(request, "App/suvform.html", {"form3":formulario3})

