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

from .models import Client

class DashboardClienteView(DetailView):
    template_name   = 'clients/dashboard/index.html'
    model           = Client

    def get_object(self):
        id_ = self.request.user.id      
        return get_object_or_404(Client, user_id=id_)