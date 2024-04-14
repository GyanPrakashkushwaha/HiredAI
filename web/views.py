from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Create your views here.
def home(request):
    return render(request=request,template_name='index.html')

def forYou(request):
    return render(request=request,template_name='foryou.html')