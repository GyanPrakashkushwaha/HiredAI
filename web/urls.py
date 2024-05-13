from django.urls import path
from . import views


urlpatterns = [
    path(route='',view=views.home,name='home'),
    path(route='upload/',view=views.upload,name='upload'),
    path(route='recommendation/',view=views.recommendation,name='recommendation'),
    path(route='profile/',view=views.profile,name='profile'),
    path(route='about/',view=views.about,name='scrap'),
    path('home/', views.home_view )
]
