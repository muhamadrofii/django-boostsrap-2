from django.shortcuts import render

def kids(request):
    return render(request, 'kids.html')

def parents(request):
    return render(request, 'parents.html')