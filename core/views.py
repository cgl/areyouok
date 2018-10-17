from django.shortcuts import render
from core.forms import InputForm
# Create your views here.

def home(request):
    form = InputForm()
    return render(request, 'core/home.html', {"form": form})

def display_results(request):
    return render(request, 'core/results.html', {"results": "results"})
