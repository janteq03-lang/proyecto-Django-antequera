from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PerfilCreationForm, PerfilEditForm


def registro_usuario(request):
    if request.method == 'POST':
        form = PerfilCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = PerfilCreationForm()
    return render(request, 'users/registro.html', {'form': form})


def perfil_detalle(request):
    return render(request, 'users/perfil_detail.html', {'perfil': request.user})




@login_required
def perfil_editar(request):
    if request.method == 'POST':
        form = PerfilEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil_detail')
    else:
        form = PerfilEditForm(instance=request.user)
    
    
    return render(request, 'users/perfil_edit.html', {'form': form})