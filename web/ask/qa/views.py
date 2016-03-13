from django.shortcuts import render

# Create your views here.
from django.http import HtttpResponse
def test(request, *args, **kwargs):
    return HtttpResponse('OK')