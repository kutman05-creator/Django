from django.shortcuts import render , get_list_or_404

# Create your views here.

from  django.http import HttpResponse
from datetime import datetime

from . import models

def book_list_view(request):
    if request.method == 'GET':
        query = models.BookModel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, 'show.html', context=context_object_name)

def book_detail_view(request, id):
    if request.method == 'GET':
        query = get_list_or_404(models.BookModel, id=id)
        context_object_name = {
            'book_id': query,

        }
        return render(request, 'show_detail.html', context=context_object_name)


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
