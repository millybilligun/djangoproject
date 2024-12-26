from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

@login_required
def page3(request):
    return render(request, 'page3.html')

def homepage(request):
    return render(request, 'homepage.html')


