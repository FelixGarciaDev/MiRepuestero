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

class HomeView(View):
    template_name = "home/index.html"
       
    def get(self, request, *args, **kwargs):
        # GET method
        context = {}      
        context["index"] = True          
        return render(request, self.template_name, context)