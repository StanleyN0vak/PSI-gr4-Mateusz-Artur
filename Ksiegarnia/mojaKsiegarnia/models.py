from django.db import models


# Create your models here.
class Gatunek(models.Model):
    nazwa: str = models.CharField(max_length=45)

    def __str__(self):
        return self.nazwa


class Autor(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pseudonim = models.CharField(max_length=45)


class Wydawnictwo(models.Model):
    nazwa = models.CharField(max_length=45)


class Ksiazka(models.Model):
    tytul: str = models.CharField(max_length=45)
    autor: str = models.CharField(max_length=45)
    dataPublikacji = models.DateField()

    class Meta:
        ordering = ('tytul',)

    def __str__(self):
        return self.tytul


class Opinie(models.Model):
    ocena = models.IntegerField(max_length=2)
    komentarz = models.TextField(max_length=200)
    dataDodania = models.DateField()


class StatusKsiazka(models.Model):
    nazwaStatusu = models.CharField(max_length=45)


class SzczegolyZamowienia(models.Model):
    cenaNetto = models.CharField(max_length=45)
    cenaBrutto = models.CharField(max_length=45)
    ilosc = models.CharField(max_length=45)
    statusZamowienia = models.CharField(max_length=45)


class Zamowienie(models.Model):
    dataZamowienia = models.DateField()


class StatusZamowienia(models.Model):
    nazwa = models.CharField(max_length=45)


class Klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    nrTelefonu = models.CharField(max_length=45)
    dataUrodzenia = models.DateField()
    login = models.CharField(max_length=45)
    haslo = models.CharField(max_length=45)
    email = models.CharField(max_length=45)


class Adres(models.Model):
    wojewodztwo = models.CharField(max_length=45)
    kodPocztowy = models.CharField(max_length=45)
    nrDomu = models.CharField(max_length=45)
    nrLokalu = models.CharField(max_length=45)
    miejscowosc = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)


def __str__(self):
    return self.choice_text
