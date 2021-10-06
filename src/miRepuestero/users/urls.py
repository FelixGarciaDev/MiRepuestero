from django.urls import path
from .views import (
    SignupChoose,
    SignupeNormalUser,
    SignupRefiller,
    linkSentView,
    VerificationView,
    ActivationFormView,
    LoginView
)

app_name = 'users'

urlpatterns = [
    path('registrarse/', SignupChoose.as_view(), name='signup-choose'),    
    path('registrarse/particular/', SignupeNormalUser.as_view(), name='signup-normal'),
    path('registrarse/repuestero/', SignupRefiller.as_view(), name='signup-refiller'),
    path('link-enviado/', linkSentView.as_view(), name='signup-linksent'),
    # user activation
    path('activation/<uidb64>/<token>/', VerificationView.as_view(), name='activation'),
    path('activation/changepassword/', VerificationView.as_view(), name='activation-change-password'),
    path('activationform/form/<int:id>/', ActivationFormView.as_view(), name='activation-form'),
    # user login
    path('login/', LoginView.as_view(), name='login')
    
]