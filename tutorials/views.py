from django.shortcuts import render
from django.views.generic import ListView
from .models import Tutorials

# Create your views here.

class TutorialsListView(ListView):
    model = Tutorials
    template_name = 'tutorials/tutorials.html'
