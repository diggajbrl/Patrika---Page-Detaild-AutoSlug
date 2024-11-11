from django.shortcuts import render
from app.models import *
# Create your views here.

def app (request) :

    newsData = News.objects.all()

    data = {
        'newsData' : newsData
    }

    return render (request, 'index.html', data)

def newsDetails (request, slug) :

    newsMore = News.objects.get(news_slug = slug)

    data = {
        'newsMore' : newsMore
    }

    return render (request, 'news.html', data)