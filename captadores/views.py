from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home (request):
    return HttpResponse('ok', status = 200)

def home2 (request):
    return render(request, 'home2.html', {'name': 'Leandro', 'time': str(datetime.now())})