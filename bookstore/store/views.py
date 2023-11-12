from django.shortcuts import render

# Create your views here.
def contents(request):
    return render(request,'store/contents.html')