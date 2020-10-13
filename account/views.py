from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Wellcome(TemplateView):
   template_name = 'accoutnt/Wellcome.html'


# class LoginView(TemplateView):
#    template_name = 'accoutnt/login.html'

