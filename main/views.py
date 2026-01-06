from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import title


# Create your views here.
def index(request):
    context = {
        'title' : 'Главная',
        'content' : 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title':'О нас',
        'content':'О нас'
    }
    return render(request, 'main/about.html', context)
