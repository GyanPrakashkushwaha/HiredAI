from django.urls import path
from . import views


urlpatterns = [
    path(route='',view=views.home),
    path(route='foryou/',view=views.forYou,name='forYou'),
    path(route='hello/',view=views.hello,name='hello')
]
