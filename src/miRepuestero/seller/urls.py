from django.urls import path
from .views import (
    DashboardSellerView,
    DashboardPublicacionesListView,
    DashboardNuevaPublicacionView,
    DashboardUpdatePublicacionView,
    DashboardDeletePublicacionView,
)

app_name = 'seller'

urlpatterns = [
    path('mi-cuenta/', DashboardSellerView.as_view(), name='dashboard'),
    # publications url´s
    path('inventario/', DashboardPublicacionesListView.as_view(), name='inventory'),
    path('nueva-publicacion/', DashboardNuevaPublicacionView.as_view(), name='create-publication'),
    path('editar-publicacion/<int:id>/', DashboardUpdatePublicacionView.as_view(), name='update-publication'),
    path('eliminar-publicacion/<int:id>/', DashboardDeletePublicacionView.as_view(), name='delete-publication'),

]