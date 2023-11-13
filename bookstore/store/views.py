from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


def contents(request):
    return render(request,'store/contents.html')


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

