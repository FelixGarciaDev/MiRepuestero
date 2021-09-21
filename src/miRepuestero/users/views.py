from typing import Protocol
from django.http import HttpResponse

from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth import get_user_model

# email verification and password reset stuff
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from django.template.loader import render_to_string

from django.core.mail import EmailMessage

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

from .tokens import token_generator

from .forms import SignupForm

#from users.models import Cliente, Publicacion, Repuestero

User = get_user_model()
# -----------------------------------------------------------------------
class SignupChoose(View):
    template_name = "users/index.html"

    def get(self, request, *args, **kwargs):
        # GET method
        context = {}              
        return render(request, self.template_name, context)

class SignupeNormalUser(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'users/signup/index.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'normal'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # if form valid, create a inactive user with empty password        
        user = form.save(commit=False)
        user.is_active = False
        user.is_cliente = True
        user.password1 = ''
        user.password2 = ''
        user.save()                
        # send confirmation email
        to_email        = form.cleaned_data.get('email')
        uidb64          = urlsafe_base64_encode(force_bytes(user.pk))
        token           = token_generator.make_token(user)        
        domain          = get_current_site(self.request).domain
        link            = reverse('superuser:activation', kwargs={'uidb64':uidb64, 'token': token})
        protocol        = 'http://'
        activate_url    = protocol+domain+link
        email_subject   = '[MiRepuestero.com] ¡Ya casi tienes todos los repuestos a un click!'
        emai_body       = 'Bienvenido a MiRepuestero activa tu cuenta haciendo click en el siguiente enlace\n\n'+activate_url
        send_mail(
            email_subject, 
            emai_body,
            'noreply@mirepuestero.com',
            #[user], #recipients list
            [to_email],
            fail_silently=False,
        )
        #redirigo al usuario a una pantalla que informa que le fue enviado un correo de activación            
        return redirect('refillers:signup-repuestero-linksent')

class SignupRefiller(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'users/signup/index.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'refiller'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        # if form valid, create a inactive user            
        user = form.save(commit=False)
        user.is_active = False
        user.is_repuestero = True
        user.save() 
        # send confirmation email            
        current_site = get_current_site(self.request)            
        subject = '[MiRepuestero.com] ¡Ya casi estas listo para publicar en MiRepuestero.com!'
        message = render_to_string('refillers/signup/signup_activation_repuestero_email.html', {
            'user': user,
            'domain': current_site.domain,                
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': account_activation_token.make_token(user),
        })            
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(subject, message, to=[to_email])
        email.send()
        #redirigo al usuario a una pantalla que informa que le fue enviado un correo de activación            
        return redirect('refillers:signup-repuestero-linksent')