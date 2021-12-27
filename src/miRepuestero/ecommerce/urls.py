from django.urls import path
from .views import (
    EcommerceListView
)

app_name = 'ecommerce'

urlpatterns = [
    path('busqueda/', EcommerceListView.as_view(), name='search'),
]