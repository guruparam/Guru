from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from show.forms import brandform, modelform,Transactionform
from show.models import Brand,Transaction,Phonemodel
from django.db.models import Max, Avg, Sum, Min, Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def displayview(request):
    return render(request,'display.html')


def msg(request):
    return render(request,'msg.html')

@login_required(login_url="/customer/login/")
def create_brand(request):
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
    

@login_required(login_url="/customer/login/")
def create_model(request):
    try:
        if request.method == 'POST':
            model = modelform(request.POST,request.FILES)
            if model.is_valid():
               model.save()
               return redirect('message')
        else:
            model = modelform()
        return render(request,'index1.html',{'form': model})
    except:
        return HttpResponse("You Enter the Invalid Input")
    

def list_brand(request): 
    brand = Brand.objects.all()
    paginator = Paginator(brand, 5)

    page = request.GET.get('page')
    try:
        brands = paginator.page(page)
    except PageNotAnInteger:
        brands = paginator.page(1)
    except EmptyPage:
        brands = paginator.page(paginator.num_pages)

    context = {'brand' : brands}
    return render(request, 'list1.html' , context)


def list_model(request):
    model = Phonemodel.objects.all()
    paginator = Paginator(model, 6)

    page = request.GET.get('page')
    try:
        models = paginator.page(page)
    except PageNotAnInteger:
        models = paginator.page(1)
    except EmptyPage:
        models = paginator.page(paginator.num_pages)

    context = {'model' : models}
    return render(request,'list2-1.html',context)


def list_model1(request,brand_id):
    try:
        if (Brand.objects.filter(name=brand_id)):
            model = Phonemodel.objects.filter(brand__name=brand_id).order_by('created_at')
            context = {"model":model}
            return render(request,'list2.html',context)
        else:
            messages.warning(request,'No such Models Found')
            return redirect('List_brand')
    except:
        messages.warning(request,'Model Page Does Not Load')
        

@login_required(login_url="/customer/login/")
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
                if model.available_quantities == 0:
                    return HttpResponse("Sorry, please visit next time")
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
        messages.ERROR(request,'Warning! Please visit after some time...')



@login_required(login_url="/customer/login/")
def statics(request):
    result = Transaction.objects.all()
    Total_Sell = Transaction.objects.count()
    
    Top_Sell_Phone = Phonemodel.objects.annotate(num_sold = Count('transaction')).order_by('-num_sold').first()
    
    Top_sell_brand = Brand.objects.annotate(num_sold=Count('phonemodel__transaction')).order_by('-num_sold').first()

    Top_valued_brand = Brand.objects.annotate(tot_price=Sum('phonemodel__transaction__amount')).order_by('-tot_price').first()

    Top_valued_phone = Phonemodel.objects.annotate(tot_price=Sum('transaction__amount')).order_by('-tot_price').first()
    
    top_sell_ph_count = Top_Sell_Phone.transaction_set.count()
   
    context = {'top_sell':Top_Sell_Phone,
               'results':result,
               'tot': Total_Sell,
               'top_sell_brand':Top_sell_brand,
               'top_valued_brand':Top_valued_brand,
               'top_valued_phone':Top_valued_phone,
               'top_sell_ph_count':top_sell_ph_count,}
    
    return render(request,'statics.html',context)


def retrive_record(request):
    brand = Brand.objects.all()
    model = Phonemodel.objects.all()
    context = {'brand':brand,
               'model':model}
    return render(request,'retrive.html', context)

def update_brand(request, name):
    data = get_object_or_404(Brand, name=name)
    if request.method == 'POST':
        form = brandform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            print('Updated Successfully')
            return redirect('Update_record')
    else:
        form = brandform(instance=data)
    return render(request, 'update.html', {'form': form})
 

def update_model(request, id):
    data = get_object_or_404(Phonemodel, id=id)
    if request.method == 'POST':
        form = modelform(request.POST, instance=data)

        if form.is_valid():
            form.save()
            print('Updated Successfully')
            return redirect('Update_record')       
    else:
        form = modelform(instance=data)
    return render(request, 'update_model.html', {'form': form})

def delete_brand(request, name):
    brand = Brand.objects.get(name=name)
    brand.delete()
    return redirect('Update_record')
def delete_model(request, id):
    model = Phonemodel.objects.get(id=id)
    model.delete()
    return redirect('Update_record')

