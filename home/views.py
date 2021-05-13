from django.shortcuts import render
from .models import Feature
from django.views.generic import ListView
# Create your views here.

class Home(ListView):
    model = Feature
    template_name = 'home/home.html'
    # return render(request, 'home/home.html', {'obj': model})