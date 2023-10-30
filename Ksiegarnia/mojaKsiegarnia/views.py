from django.shortcuts import render

import mojaKsiegarnia.models


# Create your views here.
def home(request):
    return render(request, "home.html")

def ksiazki(request):
    items = mojaKsiegarnia.models.Ksiazka.objects.all()
    return render(request, "home.html", {"ksiazki": items})
