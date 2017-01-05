from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def signup(request):
    pass

def signin(request):
    pass