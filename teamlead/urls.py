from django.urls import path

from . import views

app_name = 'teamlead'

urlpatterns = [
    path('', views.index, name='index'),
    path('demand/', views.demand, name='demand'),
    path('geography/', views.geography, name='geography'),
    path('latest_vacancies/', views.latest_vacancies, name='latest_vacancies'),
    path('skills/', views.skills, name='skills'),
    
]