from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
def home(request):
    return render(request, "home.html")


def ListaKsiazek(request):
    ksiazki = Ksiazka.objects.all()
    return render(request, "home.html", {"ksiazki": ksiazki})


class KsiazkaViewSet(viewsets.ModelViewSet):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerialzer
    permission_classes = [IsAdminUser]


class GatunekViewSet(viewsets.ModelViewSet):
    queryset = Gatunek.objects.all()
    serializer_class = GatunekSerializer



class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class WydawnictwoViewSet(viewsets.ModelViewSet):
    queryset = Wydawnictwo.objects.all()
    serializer_class = WydawnictwoSerializer


class OpinieViewSet(viewsets.ModelViewSet):
    queryset = Opinie.objects.all()
    serializer_class = OpinieSerializer


class StatusKsiazkaViewSet(viewsets.ModelViewSet):
    queryset = StatusKsiazka.objects.all()
    serializer_class = StatusKsiazkaSerializer


class SzczegolyZamownieniaViewSet(viewsets.ModelViewSet):
    queryset = SzczegolyZamowienia.objects.all()
    serializer_class = SzczegolyZamowieniaSerializer


class ZamowienieViewSet(viewsets.ModelViewSet):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer


class StatusZamowienia(viewsets.ReadOnlyModelViewSet):
    queryset = StatusZamowienia.objects.all()
    serializer_class = StatusZamowieniaSerializer


class KlientViewSet(viewsets.ModelViewSet):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class AdresViewSet(viewsets.ModelViewSet):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer