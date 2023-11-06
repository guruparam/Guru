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
    try:
        if request.method == 'POST':
            brand = brandform(request.POST,request.FILES)
            if brand.is_valid():
                brand.save()
                return redirect('/create_brand')
        else:        
           brand = brandform()
           
        return render(request,'index.html', {'form': brand})
    except:
        return HttpResponse("You Enter the Invalid Input")

def create_model(request):
    try:
        if request.method == 'POST':
            model = modelform(request.POST,request.FILES)
            if model.is_valid():
               model.save()
               return redirect('/create_model')
        else:
            model = modelform()
        return render(request,'index.html',{'form': model})
    except:
        return HttpResponse("You Enter the Invalid Input")

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
    try:
        if (Brand.objects.filter(name=brand_id)):
            model = Phonemodel.objects.filter(brand__name=brand_id)
            context = {"model":model}
            return render(request,'list2.html',context)
        else:
            messages.warning(request,'No such Models Found')
            return redirect('List_brand')
    except:
        messages.warning(request,'Model Page Does Not Load')

def transaction(request, mname):
    try:
        if (Phonemodel.objects.filter(name=mname)):
            models = Phonemodel.objects.filter(name=mname).first()
            form = Transactionform
            context = {"model":models,
                       "form": form}
        try:
            if request.method == 'POST':
                model = Phonemodel.objects.get(name=mname)
                model.available_quantities -= 1
                model.save()
                trans_type = request.POST['transaction_type']
                form = Transaction (
                    user = request.user,
                    transaction_type = trans_type,
                    amount = model.price,
                    model = model
                )           
                form.save() 
                return redirect("List_brand")
            else:
                form = Transactionform()          
            return render(request,'transaction.html',context)
        except:
            messages.warning(request,'Page Not Found')       
    except:
        messages.ERROR