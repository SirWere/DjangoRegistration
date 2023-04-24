from django.shortcuts import render, redirect
from .models import Member


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], firstname=request.POST['firstname'], lastname=request.POST['lastname'], password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member(username=request.POST['username'], firstname=request.POST['firstname'], lastname=request.POST['lastname'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            return render(request, 'login.html')
