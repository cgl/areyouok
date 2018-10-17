from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.analyze_text import analyze_sentiment
from core.forms import InputForm

from .forms import InputForm
from .helpers import format_sentiment_analyzis_result


@login_required
def home(request):
    form = InputForm()
    return render(request, "core/home.html", {"form": form})


def display_results(request):
    form = InputForm(request.POST)
    results = {}

    if form.is_valid():
        text = form.cleaned_data.get("text", "")
        data = analyze_sentiment(text)
        if "error" in data:
            results = data
        else:
            results = format_sentiment_analyzis_result(data)

    return render(request, "core/results.html", results)
