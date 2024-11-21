from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'signUp.html')

def profil(request):
    return render(request, 'profil.html')