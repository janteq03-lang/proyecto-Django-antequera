from .models import Usuario
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 

class list_usuarios(LoginRequiredMixin, ListView): 
    model = Usuario
    template_name = 'usuarios/listar_usuario.html'
    context_object_name = 'usuarios'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("a")
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset

class Detail_usuarios(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detalle.html'
    context_object_name = 'usuario' 
    slug_field = 'code'
    slug_url_kwarg = 'code'
    
class Create_usuarios(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'tipo_documento', 'nro_documento', 'email', 'telefono']
    template_name = 'usuarios/usuario_forms.html'
    
    def get_success_url(self):
        return reverse_lazy('usuarios:usuario_detalle', kwargs={'code': self.object.code})

class Update_usuarios(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'telefono', 'email']
    template_name = 'usuarios/usuario_forms.html'
    slug_field = 'code'
    slug_url_kwarg = 'code'
    
    def get_success_url(self):
        return reverse_lazy('usuarios:usuario_detalle', kwargs={'code': self.object.code})

class Delete_usuarios(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/delete.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')