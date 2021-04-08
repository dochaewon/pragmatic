from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# 브라우저에서 접근하면 기본 출력하도록할것임

def hello_world(request):
    return render(request, 'base.html')
