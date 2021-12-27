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

from .models import Seller, Publication

from .forms import CreatePublicationForm

class DashboardSellerView(DetailView):
    template_name   = 'seller/dashboard/index.html'
    model           = Seller

    def get_object(self):
        id_ = self.request.user.id      
        return get_object_or_404(Seller, user_id=id_)

class DashboardPublicacionesListView(ListView):
    model = Publication
    ordering = ('name', )    
    template_name = 'seller/dashboard/publicationList.html'

    #Obtengo las publicaciones del usuario FORMA ANTIGUA
    """def get_queryset(self):
        queryset = self.request.user.publicaciones #esto es porque en el modelo publicaciones esta relacionado al user
        print(queryset)
        return queryset    """

    #paso por contexto información de DOS modelos repuestero y publicaciones asociadas
    def get_context_data(self, **kwargs):
        context = super(DashboardPublicacionesListView, self).get_context_data(**kwargs)
        id_ = self.request.user.id
        context = {}        
        context['repuestero'] = get_object_or_404(Seller, user=id_)
        print(context['repuestero'])
        context['publicaciones'] = self.request.user.publications.all() #esto es porque en el modelo publicaciones esta relacionado al user
        print(context['publicaciones'])
        return context

class DashboardNuevaPublicacionView(CreateView):
    model         = Publication
    form_class    = CreatePublicationForm
    template_name = 'seller/dashboard/publicationCreate.html'

    def form_valid(self, form):
        nueva_publicacion = form.save(commit=False)
        nueva_publicacion.owner = self.request.user
        nueva_publicacion.activa = True
        nueva_publicacion.save()        
        return redirect('seller:inventory')

class DashboardUpdatePublicacionView(UpdateView):
    model = Publication
    form_class    = CreatePublicationForm    
    template_name = 'seller/dashboard/publicationUpdate.html'

    def get_success_url(self):
        return reverse('seller:inventory')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Publication, id=id_)

    def form_valid(self, form):        
        return super().form_valid(form)

class DashboardDeletePublicacionView(DeleteView):
    model = Publication
    template_name = 'seller/dashboard/publicationDelete.html'
        
    def get_success_url(self):
        return reverse('seller:inventory')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Publication, id=id_)