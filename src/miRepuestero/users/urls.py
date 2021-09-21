from django.urls import path
from .views import (
    SignupChoose,
    SignupeNormalUser,
    SignupRefiller
)

app_name = 'users'

urlpatterns = [
    path('registrarse/', SignupChoose.as_view(), name='signup-choose'),    
    path('registrarse/particular/', SignupeNormalUser.as_view(), name='signup-normal'),
    path('registrarse/repuestero/', SignupRefiller.as_view(), name='signup-refiller'),
]