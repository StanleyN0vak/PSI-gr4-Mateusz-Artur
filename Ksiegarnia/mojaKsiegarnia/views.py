from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
def home(request):
    return render(request, "home.html")


def ksiazki(request):
    items = Ksiazka.tytul
    return render(request, "home.html", {"ksiazki": items})


class KsiazkaViewSet(viewsets.ModelViewSet):
    queryset = Ksiazka.objects.all()
    serializer_class = KlientSerializer
