from django.shortcuts import render


def index(request):
    data = "123"
    return render(request, 'index.html', {"data":data})
