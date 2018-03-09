from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from datetime import datetime
import requests

start_time = datetime(2018, 3, 10, 12, 0, 0, 0)
def intro(request):
    if datetime.now() < start_time:
        return render(request, "before_opening.html")
    return render(request, "intro.html")

def clue_1_5(request):
    return render(request, "clue_1_5.html")

def clue_2(request):
    return render(request, "clue_2.html")

def clue_3(request):
    return render(request, "clue_3.html")