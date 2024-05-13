from django.shortcuts import render , redirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .forms import ResumeForm , GeeksForm

# Create your views here.
def home(request):
    return render(request=request,template_name='index.html')

# def upload(request):
#     return render(request=request,template_name='upload.html')

def recommendation(request):
    return render(request=request,template_name='recommendation.html')

def profile(request):
    return render(request=request,template_name='profile.html')

def about(request):
    return render(request=request,template_name='scrap.html')

def handle_uploaded_file(f):
    with open('assets/resumes/'+f.name,'wb+') as file_:
        for chunk in f.chunks():
            file_.write(chunk)      

def upload(request):
    context = {}
    if request.POST:
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["resume_field"])
    else:
        form = ResumeForm()
    context['form'] = form
    return render( request , "upload.html",context)