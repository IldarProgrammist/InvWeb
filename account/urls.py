from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from account.views import Wellcome
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', Wellcome.as_view()),
    path('account/login/',LoginView.as_view(),  name='login'),
    path('account/logout/',LogoutView.as_view(next_page='/'),  name='logout')
]