from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'books', BookViewSet)
router.register(r'orderdetails', OrderDetailsViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'opinions', OpinionViewSet)
router.register(r'usersview', ReadOnlyUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListCreateView.as_view(), name='user-list-create')
]