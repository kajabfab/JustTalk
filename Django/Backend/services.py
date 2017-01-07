from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models


def signup(username, mobile, password):

    any_user = models.Profile.objects.filter(mobile=mobile)
    if any_user:
        return 0
    else:
        new_user = User.objects.create_user(username=username, password=password)
        new_profile = models.Profile(user=new_user, mobile=mobile)
        new_profile.save()
        return 1


def signin(user, request):

    any_user = models.Profile.objects.filter(mobile=user['mobile'])
    if any_user:
        username = any_user[0].user.username
        user_obj = authenticate(username=username, password=user['password'])
        if user_obj is not None:
            login(request, user_obj)
            return 1
        else:
            return 0
    else:
        return 0

def signout(request):
    logout(request)
    return 1
