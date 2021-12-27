from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic.base import RedirectView
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    FormView
)

from django.db.models import Q

from seller.models import Seller, Publication

class EcommerceListView(ListView):
    model = Publication
    ordering = ('name', )
    context_object_name = 'publicaciones'
    template_name = 'ecommerce/index.html'

    # def get_queryset(self):
    #     queryset = Publicacion.objects.all()        
    #     return queryset
