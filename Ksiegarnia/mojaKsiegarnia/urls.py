from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'Ksiazka', views.KsiazkaViewSet, basename='Ksiazka')
router.register(r'Gatunek', views.GatunekViewSet, basename='Gatunek')
router.register(r'Autor', views.AutorViewSet, basename='Autor')
router.register(r'Wydawnictwo', views.WydawnictwoViewSet, basename='Wydawnictwo')
router.register(r'Opinie', views.OpinieViewSet, basename='Opinie')
router.register(r'Status Ksiazka', views.StatusKsiazkaViewSet, basename='StatusKsiazka')
router.register(r'Szczegoly Zamowienia', views.SzczegolyZamownieniaViewSet, basename='SzczegolyZamowienia')
router.register(r'Status Zamowienia', views.StatusKsiazkaViewSet, basename='StatusZamowienia')
router.register(r'Zamowienie', views.ZamowienieViewSet, basename='Zamowienie')
router.register(r'Klient', views.KlientViewSet, basename='Klient')
router.register(r'Adres', views.AdresViewSet, basename='Adres')

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r'api-auth/', include('rest_framework.urls')),
    re_path(r'api/', include(router.urls)),
]