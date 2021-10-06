from django.urls import path
from .views import (
    DashboardClienteView,
)

app_name = 'clients'

urlpatterns = [
    path('mi-cuenta/', DashboardClienteView.as_view(), name='dashboard-client'),
]