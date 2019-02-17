from django.shortcuts import render


def home(request):
    return render(request, 'products/home.html')

def style(request):
    return render(request, 'products/style.html')
