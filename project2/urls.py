
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('teamlead.urls', namespace='teamlead')),
    path('admin/', admin.site.urls),
]
