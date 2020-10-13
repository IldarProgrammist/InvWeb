from django.urls import path
from main.views import *
urlpatterns = [
    path('home/',HomeViews.as_view(), name='home'),
    path('print/',  pintView, name='print'),

]