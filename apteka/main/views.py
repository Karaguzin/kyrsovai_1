from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task, Drug

# Create your views here.

links = [
    {'link': 'ORVI'}, {'link': 'Painkillers'}, {'link': 'Throat'}, {'link': 'Antipyretics'}, {'link': 'Nose'}
        ]

def get_link(request, r_slug):
    return redirect(reverse(r_slug), permanent=True)

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Apteka', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def ORVI(request):
    return render(request, 'main/ORVI.html', {'remedies': Drug.objects.filter(purpose='ОРВИ')})

def Antipyretics(request):
    return render(request, 'main/Antipyretics.html', {'remedies': Drug.objects.filter(purpose='Жаропонижающее')})

def Painkillers(request):
    return render(request, 'main/Painkillers.html', {'remedies': Drug.objects.filter(purpose='Обезболивающие')})

def Throat(request):
    return render(request, 'main/Throat.html', {'remedies': Drug.objects.filter(purpose='Горло')})

def Nose(request):
    return render(request, 'main/Nose.html', {'remedies': Drug.objects.filter(purpose='Насморк')})

def product_orvi(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)

def product_antipyretics(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)

def product_painkillers(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)

def product_throat(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)

def product_nose(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)

#Обработка ошибок
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def InternalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')

def ErrBadRequest(request, exception):
    from django.http import HttpResponseBadRequest
    return HttpResponseBadRequest('<h1>Плохой запрос</h1>')