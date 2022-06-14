from django.shortcuts import render
from datetime import datetime
from FAMILIA_APP.models import *
date_to_day=datetime.today().strftime("%d-%m-%Y")

def inicio(request):
    hoy= date_to_day
    return render(request,"index.html",{"hoy":hoy})

def Familiar_1(request):
    nombre = "Camila"
    apellido = "Almrion"
    edad = 20
    profecion = "Estudiante"
    parentesco = "Hermana"
    anio= 2022-edad
    num_quini= [8,5,2002,22,1,72]
    hoy= date_to_day
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, profecion=profecion, parentesco=parentesco, anio=anio,Telequino=num_quini,hoy=hoy)
    familiar.save
    return render(request,"Familiar_1.html",{"mi_nombre":familiar.nombre, "apellido":familiar.apellido, "edad":familiar.edad, "año_de_nacimiento":familiar.anio,"profecion":familiar.profecion,"parentesco":familiar.parentesco,"num":familiar.Telequino,"hoy":familiar.hoy})

def Familiar_2(request):

    nombre = "Martin"
    apellido = "Almrion"
    edad = 48
    profecion = "Camionero"
    parentesco = "Papa"
    anio= 2022-edad
    num_quini= [2,8,1974,17,5,4]
    hoy= date_to_day
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, profecion=profecion, parentesco=parentesco, anio=anio,Telequino=num_quini,hoy=hoy)
    familiar.save
    return render(request,"Familiar_1.html",{"mi_nombre":familiar.nombre, "apellido":familiar.apellido, "edad":familiar.edad, "año_de_nacimiento":familiar.anio,"profecion":familiar.profecion,"parentesco":familiar.parentesco,"num":familiar.Telequino,"hoy":familiar.hoy})
    

def Familiar_3(request):

    nombre = "Marcela"
    apellido = "Loizaga"
    edad = 50
    profecion = "Estudiante/Ama de casa"
    parentesco = "Mama"
    anio= 2022-edad
    num_quini= [22,1,1972,8,5,2]
    hoy= date_to_day
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, profecion=profecion, parentesco=parentesco, anio=anio,Telequino=num_quini,hoy=hoy)
    familiar.save
    return render(request,"Familiar_1.html",{"mi_nombre":familiar.nombre, "apellido":familiar.apellido, "edad":familiar.edad, "año_de_nacimiento":familiar.anio,"profecion":familiar.profecion,"parentesco":familiar.parentesco,"num":familiar.Telequino,"hoy":familiar.hoy})