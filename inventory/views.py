from typing import Any, Dict
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .models import *
import json
from django.views import generic
from django.http import JsonResponse


# Create your views here.




class HomePage(generic.ListView):
    model=Product
    context_object_name='products'
    
    template_name='base.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)

       
        context['categories']=Category.objects.all()
        context['brands']=Brand.objects.values('title').distinct()
        context['sellers']=Seller.objects.values('shop_name').distinct()
        context['warrenties']=Warrenty.objects.all()
        return context
    
    def dispatch(self, request, *args: Any, **kwargs: Any) :
        dispatch=super().dispatch(request, *args, **kwargs)
        if request.method=="POST":
            product=Product.objects.all()
            data=json.loads(request.body)
            price_from=data['price_from']
            price_to=data['price_to']
            
            categories=data['category']
            brands=data['brand']
            sellers=data['seller']
            warrenties=data['warrenty']

            if categories:
                product=product.filter(category__in=categories)

            if brands:
                product=product.filter(brand__title__in=brands)
            
            if sellers:
                product=product.filter(seller__shop_name__in=sellers)

            if warrenties:
                product=product.filter(warrenty__in=warrenties)

            if price_from and price_to:
                product=product.filter(price__gte=price_from,price__lte=price_to)    

             

           
            


            return JsonResponse({'data':list(product.values())},safe=False)

        return dispatch 

        



    




    