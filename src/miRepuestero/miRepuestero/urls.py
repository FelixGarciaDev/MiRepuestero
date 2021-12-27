from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('users.urls')),
    path('cliente/',include('clients.urls', namespace='clients')),
    path('repuestero/',include('seller.urls', namespace='seller')),
    path('',include('ecommerce.urls')),
]