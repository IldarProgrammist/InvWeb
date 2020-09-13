from django.urls import path
from main.views import *
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
]