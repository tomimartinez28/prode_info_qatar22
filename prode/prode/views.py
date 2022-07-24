from django.shortcuts import render
from equipos.models import Equipo

def inicio(request):
    equipos = Equipo.objects.all()
    ctx = {
        "equipos" : equipos
    }
    
    return render(request,"index.html", ctx)

def signin(request):
    return render(request,"signin.html", {})