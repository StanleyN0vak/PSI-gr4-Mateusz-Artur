from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ksiazka', views.KsiazkaViewSet, basename='ksiazka')

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r'api-auth/', include('rest_framework.urls')),
    re_path(r'api/', include(router.urls)),
]