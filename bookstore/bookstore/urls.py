from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('about', views.about),
    path('', views.homepage),
    path('bookstore', views.bookstore)
]
