from django.shortcuts import render
from .models import indexPage

def index(request):
    template = 'index.html'
    pageObj = indexPage.objects.first()
    context = {
        'pageObj': pageObj
    }
    return render(request, template, context)

def demand(request):
    template = 'index.html'
    context = {

    }
    return render(request, template, context)

def geography(request):
    template = 'geography.html'
    context = {

    }
    return render(request, template, context)

def latest_vacancies(request):
    template = 'index.html'
    context = {

    }
    return render(request, template, context)

def skills(request):
    template = 'index.html'
    context = {

    }
    return render(request, template, context)



