from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from show.forms import brandform, modelform,Transactionform
from show.models import Brand,Transaction,Phonemodel
from django.contrib import messages
from django.contrib.auth.models import User
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
           
    return render(request,'index.html', {'form': brand})

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

def transaction(request, mname):
    if (Phonemodel.objects.filter(name=mname)):
        models = Phonemodel.objects.filter(name=mname).first()
        phonemodel = Phonemodel.objects.get(name=mname)
        form = Transactionform(phonemodel=phonemodel)
        context = {"model":models,
                   "form": form}
        if request.method == 'POST':
           form = Transactionform(request.POST)
           if form.is_valid():
            # Get the current user and the amount from the PhoneModel models
               
               form.save()
               
            # Redirect to a new URL after the transaction is added
               return HttpResponse('You got the Order Successfully')

        else:
           form = Transactionform()
           
        return render(request,'transaction.html',context)
    else:
        messages.warning(request,'No such Models Found')
        return redirect('List_model')