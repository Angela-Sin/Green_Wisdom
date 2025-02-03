from django.views.generic import TemplateView
from django.shortcuts import render, redirect



class Index(TemplateView):
    template_name = 'home/index.html'