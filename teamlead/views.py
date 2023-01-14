from django.shortcuts import render
from .models import indexPage, demandAd, geographyAd, skillsAd, latestAd

def index(request):
    template = 'index.html'
    pageObj = indexPage.objects.first()
    context = {
        'pageObj': pageObj
    }
    return render(request, template, context)

def demand(request):
    template = 'demand.html'
    pageObj = demandAd.objects.first()
    context = {
        'pageObj': pageObj
    }
    return render(request, template, context)

def geography(request):
    pageObj = geographyAd.objects.first()
    template = 'geography.html'
    context = {
        'pageObj': pageObj
    }
    return render(request, template, context)

def latest_vacancies(request):
    pageObj = latestAd.objects.first()
    template = 'latest_vacancies.html'
    context = {
        'pageObj': pageObj
    }
    return render(request, template, context)

def skills(request):
    pageObj = skillsAd.objects.first()
    template = 'skills.html'
    context = {
        'pageObj': pageObj
    }
    return render(request, template, context)


