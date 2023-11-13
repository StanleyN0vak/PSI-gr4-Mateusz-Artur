from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .import views


router = DefaultRouter()
router.register(r'Address', views.AddressViewSet, basename='Address')


urlpatterns = [
    path('', views.contents),
    re_path(r'api-auth/', include('rest_framework.urls')),
    re_path(r'api/', include(router.urls))
]
