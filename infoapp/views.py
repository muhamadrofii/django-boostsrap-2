from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def berita(request):
    return render(request, 'berita.html')

def tentangKami(request):
    return render(request, 'tentangKami.html')

def faq(request):
    return render(request, 'faq.html')