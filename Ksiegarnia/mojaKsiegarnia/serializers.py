from rest_framework import serializers
from mojaKsiegarnia.models import *


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'


class KlientSerializer(serializers.Serializer):
    class Meta:
        model = Klient
        fields = '__all__'


class ZamowienieSerializer(serializers.Serializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'


class StatusZamowieniaSerializer(serializers.Serializer):
    class Meta:
        model = StatusZamowienia
        fields = '__all__'


class SzczegolyZamowieniaSerializer(serializers.Serializer):
    class Meta:
        model = SzczegolyZamowienia
        fields = '__all__'


class KsiazkaSerialzer(serializers.Serializer):
    class Meta:
        model = Ksiazka
        fields = '__all__'


class GatunekSerializer(serializers.Serializer):
    class Meta:
        model = Gatunek
        fields = '__all__'


class StatusKsiazkaSerializer(serializers.Serializer):
    class Meta:
        model = StatusZamowienia
        fields = '__all__'


class AutorSerializer(serializers.Serializer):
    class Meta:
        model = Autor
        fields = '__all__'


class WydawnictwoSerializer(serializers.Serializer):
    class Meta:
        model = Wydawnictwo
        fields = '__all__'


class OpinieSerializer(serializers.Serializer):
    class Meta:
        model = Opinie
        fields = '__all__'
