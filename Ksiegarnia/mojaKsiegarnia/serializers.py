from rest_framework import serializers
import datetime
import string
from mojaKsiegarnia.models import Ksiazka, Klient, Autor, Adres, Gatunek, Wydawnictwo, Opinie, Zamowienie, \
    StatusZamowienia, SzczegolyZamowienia, StatusKsiazka


class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = '__all__'


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'


class WydawnictwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wydawnictwo
        fields = '__all__'


class GatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatunek
        fields = '__all__'


class OpinieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinie
        fields = '__all__'


class ZamowienieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'


class StatusZamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusZamowienia
        fields = '__all__'


class SzczegolyZamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SzczegolyZamowienia
        fields = '__all__'


class StatusKsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusKsiazka
        fields = '__all__'