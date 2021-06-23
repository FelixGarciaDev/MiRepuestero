from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    FormView
)

import json

class HomeView(View):
    template_name = "home/index.html"

    """def get(self, request, *args, **kwargs):
        # GET method        
        #Precio definido por el repuestero
        dolar       = json.loads(open('./static/js/trumps.json').read())
        trump_price = dolar["price"]
        localBS     = int(trump_price)*20
        expertBS    = int(trump_price)*50	
        unlimitedBS = int(trump_price)*100
        context={}        
        context["localBS"] = localBS
        context["expertBS"] = expertBS
        context["unlimitedBS"] = unlimitedBS
        return render(request, self.template_name, context)"""
    
    def get(self, request, *args, **kwargs):
        # GET method
        context = {}                
        return render(request, self.template_name, context)