from django.urls import path
from main.views import *


urlpatterns = [
    # path('home/',HomeViews.as_view(), name='home'),
    path('home/', homeView, name='home'),
    path('home/print/',  PrintView.as_view(), name='print'),


]