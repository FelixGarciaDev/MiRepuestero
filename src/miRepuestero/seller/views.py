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

from .models import Seller

class DashboardSellerView(DetailView):
    template_name   = 'seller/dashboard/index.html'
    model           = Seller

    def get_object(self):
        id_ = self.request.user.id      
        return get_object_or_404(Seller, user_id=id_)