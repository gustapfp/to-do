from django.shortcuts import render
from django.http import request


def index(request):
    #return HttpResponse("Hello!")
    return render(request, 'index.html')