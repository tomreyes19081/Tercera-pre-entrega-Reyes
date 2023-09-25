from django.urls import path
from .views import *

urlpatterns=[
    path("inicio/", inicio, name="Inicio"),
    path("sedan/", ver_sedan, name="VerSedan"),
    path("coupe/",ver_coupe, name="VerCoupe"),
    path("suv/", ver_suv, name="VerSuv"),
    path("sedanform/", sedanformulario, name="Formsedan"),
    path("buscarmodelo/", busquedamodelo, name="Buscarmodelo"),
    path("resultado/", Resultado, name="Resultadobusqueda"),
    path("coupeform/", coupeformulario, name="Formcoupe"),
    path("suvform/", suvformulario, name="Formsuv"),

    ]