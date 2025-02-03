from django.shortcuts import render

# Create your views here.

from  django.http import HttpResponse
from datetime import datetime


def about_me(request):
    if request.method == "GET":
        return HttpResponse("About me")


def text_and_photo(request):
    if request.method == "GET":
        return HttpResponse("Я СТАНУ КОРОЛЕМ ПИРАТОВ !"
                            '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZUTt3Ekktjt6sFKvqEEzWqgLnMduBo_znDQ&s" />')


def system_time(request):
    if request.method == "GET":
        current_time = datetime.now()
        return HttpResponse("current time : " + current_time.strftime("%Y-%m-%d %H:%M:%S"))
