from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.


def index(request):
    form1 = UserForm()
    return render(request, 'index.html', {'form': form1})


def zapros(request):
    data = request.POST.get('name')
    return HttpResponse(f'<h1>Привет, {data}!</h1>')
