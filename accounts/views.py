from django.shortcuts import render

from .forms import PozosForm

# from example
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def reporta(request):
    form = PozosForm()
    if request.method == 'POST':

        # debugging
        print(request)

        # save if valid
        form = PozosForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/reporta.html', context)

def mapa(request):
    return render(request, 'accounts/mapa.html')
