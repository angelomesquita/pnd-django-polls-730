from django.shortcuts import render
from django.http import HttpResponse

# View index /
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")