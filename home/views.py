from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse



class Index(TemplateView):
    template_name = 'home/index.html'