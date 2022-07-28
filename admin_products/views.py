from django.shortcuts import render, redirect
from .models import Products
from .forms import admin_product_form
from main import views
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from calculator.models import sub_user_details

import sweetify




def site_owner(request):
    
    
    if not request.user.is_superuser:
        sweetify.error(request, title='Only Site Owners can do this')
        return redirect('/')
    else:   
        form = admin_product_form(request.POST or None, request.FILES or None)
     
    
        if form.is_valid():
       
            form.save()
            sweetify.success(request, title='Product added')
        else: 
            sweetify.error(request, title='Product already exists')
    
    subscribers = sub_user_details.objects.all()
    product_details = Products.objects.all()
    context={'form':form,
             'product_details':product_details,
             'subscribers':subscribers}
    template = 'product_add.html'
    return render(request,template , context)



##def delete_item(request):
    