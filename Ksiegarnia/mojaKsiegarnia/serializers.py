from rest_framework import serializers
from mojaKsiegarnia.models import *


class Adres(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'


class Klient(serializers.Serializer):
    class Meta:
        model = Klient
        fields = '__all__'


class Zamowienie(serializers.Serializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'


class StatusZamowienia(serializers.Serializer):
    class Meta:
        model = StatusZamowienia
        fields = '__all__'


class SzczegolyZamowienia(serializers.Serializer):
    class Meta:
        model = SzczegolyZamowienia
        fields = '__all__'


class Ksiazka(serializers.Serializer):
    class Meta:
        model = Ksiazka
        fields = '__all__'


class Gatunek(serializers.Serializer):
    class Meta:
        model = Gatunek
        fields = '__all__'


class StatusKsiazka(serializers.Serializer):
    class Meta:
        model = StatusZamowienia
        fields = '__all__'


class Autor(serializers.Serializer):
    class Meta:
        model = Autor
        fields = '__all__'


class Wydawnictwo(serializers.Serializer):
    class Meta:
        model = Wydawnictwo
        fields = '__all__'


class Opinie(serializers.Serializer):
    class Meta:
        model = Opinie
        fields = '__all__'
