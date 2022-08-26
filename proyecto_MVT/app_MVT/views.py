from django.shortcuts import render
from app_MVT.models import Familiar
from django.http import HttpResponse

# Create your views here.
def family(self):
    padre = Familiar(nombre="Jose", edad = "77", cumple = "2022-10-08")
    padre.save()
    madre = Familiar(nombre="Josefina", edad="69", cumple="2022-03-12")
    madre.save()
    marido = Familiar(nombre="Juan", edad="30", cumple="2022-09-17")
    marido.save()

    documento_flia = f"Nombre pa: {padre.nombre}   Edad pa: {padre.edad}   Cumple pa: {padre.cumple} <br><br> Nombre ma: {madre.nombre}   Edad ma: {madre.edad}   Cumple ma: {madre.cumple} <br><br> Nombre rido: {marido.nombre}   Edad rido: {marido.edad}   Cumple rido: {marido.cumple}"

    return HttpResponse(documento_flia)