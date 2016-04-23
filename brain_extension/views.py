from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render

def login(request):
    return render(request,'login.html',{})

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/tasks')
    else:
        return HttpResponseRedirect('/doo')
