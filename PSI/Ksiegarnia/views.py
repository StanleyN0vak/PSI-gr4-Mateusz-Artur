from django.shortcuts import render

# Create your views here.
from django.core.exceptions import PermissionDenied


def index(request):
    """homepage of learning logs"""
    return render(request,'Ksiegarnia/index.html')