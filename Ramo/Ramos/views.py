from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .forms import RamoForm
from Ramos.models import Ramo, Ramito, Flor
from django.contrib.auth.decorators import login_required

def listar_ramos(request):
    fl=Ramo.objects.all()
    return render(request,'listar_Ramos.html',{'fl':fl})

def detalle_ramo(request,pk):
        p=get_object_or_404(Ramo, pk=pk)
        return render(request,'detalle_ramo.html', {'p':p})
def detalle_flor(request,pk):
    p=get_object_or_404(Flor, pk=pk)
    return render(request,'detalle_flor.html', {'p':p})

def listar_flores(request):
    fl=Flor.objects.all()
    return render(request,'listar_flores.html',{'fl':fl})

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
