from django.shortcuts import render
from .models import *


def main(request):
    return render(request, 'bodyapp/main.html')