from typing import Protocol
from django.http import HttpResponse

from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

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

from .forms import SignupForm, SignupByMailForm, UserUpdatePassWordForm

from clients.models import Client

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
    form_class = SignupByMailForm
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
        link            = reverse('users:activation', kwargs={'uidb64':uidb64, 'token': token})
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
        print("mail send")
        #redirigo al usuario a una pantalla que informa que le fue enviado un correo de activación            
        return redirect('users:signup-linksent')

class SignupRefiller(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'users/signup/index.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'refiller'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        # if form valid, create a inactive user
        print("form valid")            
        print(form)
        user = form.save(commit=False)
        user.is_active = False
        user.is_repuestero = True
        user.save() 
        # send confirmation email            
        # send confirmation email
        to_email        = form.cleaned_data.get('email')
        uidb64          = urlsafe_base64_encode(force_bytes(user.pk))
        token           = token_generator.make_token(user)        
        domain          = get_current_site(self.request).domain
        link            = reverse('N:activation', kwargs={'uidb64':uidb64, 'token': token})
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
        print("mail send")
        #redirigo al usuario a una pantalla que informa que le fue enviado un correo de activación            
        return redirect('users:signup-refiller-linksent')

class linkSentView(View):
    template_name = "users/signup/linkSent.html"
    def get(self, request, *args, **kwargs):
        # GET method        
        context = {}
        return render(request, self.template_name, context)

class VerificationView(View):

    def get(self, request, uidb64, token):
        try:            
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)            
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None        
        if user is not None and token_generator.check_token(user, token):
            # activate user and login:
            user.is_active = True
            user.save()
            login(request, user)
            if user.is_cliente:
                client = Client.objects.create(user=user)
            # if user.is_repuestero:
            #     refiller = Repuestero.objects.create(user=user)
            return render(request, 'users/signup/activationSuccess.html')
        else:
            return HttpResponse('¡Link invalido o expirado!')

    def post(self, request):
        form = UserUpdatePassWordForm(request.POST)
        if form.is_valid():
            print("form valid")
            #user = form.save()
            user = self.request.user
            print("got user")
            print(user)
            print(form.cleaned_data['password1'])
            user.set_password(form.cleaned_data['password1'])
            print("password was set")
            user.save()
            #update_session_auth_hash(request, user) # Important, to update the session with the new password
            return HttpResponse('Password changed successfully')

class ActivationFormView(UpdateView):
    model           = User
    template_name   = 'superuser/activation/activationValid.html'
    form_class      = UserUpdatePassWordForm 

    def get_object(self):                
        id_     = self.kwargs.get("id")
        return get_object_or_404(Employee, user_id=id_)   

class LoginView(FormView):
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user
            user = form.get_user()
            if user is not None and user.is_cliente:
                login(request, user)
                return redirect('clients:dashboard-client')
            if user is not None and user.is_repuestero:
                login(request, user)
                return redirect('refillers:dashboard-client')
            context = {'form':form}
            return render(request, self.template_name, context)