from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .forms import RamoForm, FlorForm
from Ramos.models import Ramo, Ramito, Flor
from django.contrib.auth.decorators import login_required
def listar_ramos(request):
    fl=Ramo.objects.all()
    return render(request,'listar_Ramos.html',{'fl':fl})

def detalle_ramo(request,pk):
        p=get_object_or_404(Ramo, pk=pk)
        datos=[]
        fl=Ramito.objects.filter(ramo_id=pk)
        for fl in fl :
            nflor = Flor.objects.get(pk=fl.flor_id)
            datos.append (nflor)
        return render(request,'detalle_ramo.html', {'p':p,'datos':datos})
def detalle_flor(request,pk):
    p=get_object_or_404(Flor, pk=pk)
    return render(request,'detalle_flor.html', {'p':p})

@login_required
def Flor_nuevo(request):
  if request.method == "POST":
     formulario = FlorForm(request.POST)
     if formulario.is_valid():
        flor = Flor.objects.create(nombre=formulario.cleaned_data['nombre'],caracteristica=formulario.cleaned_data['caracteristica'],color=formulario.cleaned_data['color'],precio=formulario.cleaned_data['precio'])
     return redirect('flor',pk=flor.id)
  else:
      formulario = FlorForm()
  return render(request, 'flor_nuevo.html', {'formulario': formulario})

@login_required
def editar_flor(request, pk):
    flor = get_object_or_404(Flor, pk=pk)
    if request.method == "POST":
        formulario = FlorForm(request.POST, instance=flor)
        if formulario.is_valid():
            flor = formulario.save(commit=False)
            flor.save()
            return redirect('flor', pk=flor.id)
    else:
       formulario = FlorForm(instance=flor)
    return render(request, 'flor_nuevo.html', {'formulario': formulario})


def listar_flores(request):
    fl=Flor.objects.all()
    return render(request,'listar_flores.html',{'fl':fl})

@login_required
def eliminar_flor(request, pk):
    f = get_object_or_404(Flor, pk=pk)
    f.delete()
    return redirect('/')

@login_required
def eliminar_ramo(request, pk):
    r = get_object_or_404(Ramo, pk=pk)
    r.delete()
    return redirect('/')
@login_required    
def ramo_nuevo(request):
  if request.method == "POST":
     formulario = RamoForm(request.POST)
     f=request.POST.getlist('flores')
     p=Flor.objects.all()
     tprecio=0
     for f in f :
         nflor = Flor.objects.get(pk=f)
         tprecio=nflor.precio+tprecio
     if formulario.is_valid():
        ramo = Ramo.objects.create(nombre=formulario.cleaned_data['nombre']  , total =tprecio)
        for flor_id in request.POST.getlist('flores'):
            ramito = Ramito(flor_id=flor_id, ramo_id = ramo.id)
            ramito.save()
     return redirect('ramo', pk=ramo.pk)
  else:
      formulario = RamoForm()
  return render(request, 'ramo_nuevo.html', {'formulario': formulario})
