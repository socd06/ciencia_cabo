from django.shortcuts import render
# from example
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def reporta(request):
    return render(request, 'accounts/reporta.html')

def mapa(request):
    return render(request, 'accounts/mapa.html')
