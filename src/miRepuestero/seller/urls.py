from django.urls import path
from .views import (
    DashboardSellerView,
)

app_name = 'seller'

urlpatterns = [
    path('mi-cuenta/', DashboardSellerView.as_view(), name='dashboard'),
]