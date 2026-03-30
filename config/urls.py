from django.contrib import admin
from django.urls import path

def home(request):
    from django.http import HttpResponse
    return HttpResponse("Chat app running 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]