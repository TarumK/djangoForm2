from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User

# Create your views here.


def index(request):
    # if request.method != 'POST':
    #Выводит пустую форму регистрации.
    # form = UserCreationForm()
    form1 = UserForm()
    return render(request, 'index.html', {'form': form1})
    # else:
    #     return HttpResponse('Нажато на сабмит')



def zapros(request):
    data = request.POST.get('name')
    data2 = request.POST.get('f_lname')
    rec = User()
    rec.lname = data2
    rec.save()
    return HttpResponse(f'<h1>Привет, {data} {data2}!</h1>')
