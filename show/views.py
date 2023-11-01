from django.shortcuts import render, redirect
from django.http import HttpResponse
from show.forms import *
from show import models
from django.contrib import messages
# Create your views here.

def displayview(request):
    return render(request,'display.html')

def create_brand(request,*args, **kwargs):
    if request.method == 'POST':
        brand = brandform(request.POST,request.FILES)
        if brand.is_valid():
            brand.save()
            return redirect('/create_brand')
    else:        
       brand = brandform()
       context =  {'form': brand}   
    return render(request,'index.html',context)

def create_model(request):
    if request.method == 'POST':
        model = modelform(request.POST,request.FILES)
        if model.is_valid():
            model.save()
            return redirect('/create_model')
    else:
        model = modelform()
    return render(request,'index.html',{'form': model})

def update_model(request):
    return render(request,'update.html')

def list_brand(request):
    brand = Brand.objects.all()
    context = {"brand":brand}
    return render(request,'list1.html',context)

def list_model(request):
    model = Phonemodel.objects.all()
    context = {"model":model}
    return render(request,'list2.html',context)

def list_model1(request,brand_id):
    if (Brand.objects.filter(name=brand_id)):
        model = Phonemodel.objects.filter(brand__name=brand_id)  
        context = {"model":model}
        return render(request,'list2.html',context)
    else:
        messages.warning(request,'No such Models Found')
        return redirect('List_brand')

def transaction(request):
    return render(request,'transaction.html')    