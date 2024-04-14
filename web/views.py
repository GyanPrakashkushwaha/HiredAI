from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Create your views here.
def home(request):
    return render(request=request,template_name='index.html')

def forYou(request):
    return render(request=request,template_name='foryou.html')

def recommendation(request):
    return render(request=request,template_name='recommendation.html')

def profile(request):
    return render(request=request,template_name='profile.html')

def about(request):
    return render(request=request,template_name='about.html')
