from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Captador
from .forms import CaptadorForm

# Create your views here.
def home (request):
    captadores = Captador.objects.all()
    return HttpResponse('ok', status = 200)

def home2 (request):
    return render(request, 'home2.html', {'name': 'Leandro', 'time': str(datetime.now())})

def form_captador(request):
    form = CaptadorForm()
    return render(request, 'form_captador.html', {'form': form})

# create a new Captador
def criar_captador(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        bobina = request.POST['bobina']
        instrumento = request.POST['instrumento']

        captador = Captador()
        captador.marca = marca
        captador.bobina = bobina
        captador.instrumento = instrumento
        captador.save()
        return render(request, 'sucesso_criacao_captador.html', locals())

#read captadores 

def lista_captadores(request):
    bobina = request.GET.get('bobina')
    if bobina is None:
        captadores = Captador.objects.all()
    else:
        captadores = Captador.objects.filter(bobina=bobina)

    return render(request, 'lista_captadores.html', locals())