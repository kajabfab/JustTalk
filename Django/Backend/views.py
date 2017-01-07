from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from . import services


# Create your views here.
def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World!")


def signup(request):
    if request.method == 'POST':
        # print json.loads(request.body)
        user = json.loads(request.body)

        status = services.signup(user['username'], user['mobile'], user['password'])
        if status == 1:
            return HttpResponse("Signup OK")
        else:
            return HttpResponseBadRequest("Not good")


def signin(request):
    if request.method == 'POST':
        # print json.loads(request.body)
        user = json.loads(request.body)
        status = services.signin(user, request)
        if status == 1:
            return HttpResponse("Signin OK")
        else:
            return HttpResponseBadRequest("Not good")


def signout(request):
    if request.method == 'POST':
        # print json.loads(request.body)
        user = json.loads(request.body)
        status = services.signout(request)
        if status == 1:
            return HttpResponse("Signout OK")
        else:
            return HttpResponseBadRequest("Not good")


def forum(request):
    if request.method == 'GET':
        # chat_request =
        pass
