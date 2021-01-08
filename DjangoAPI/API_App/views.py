from django.shortcuts import render
from django.http import JsonResponse
from .models import Article
from django.core import serializers   
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def articles(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        return JsonResponse({
            "articles" : serializers.serialize('json',articles)
        })
    elif request.method == 'POST':
        data = json.loads(request.body)
        new_article = Article.objects.create(name = data['name'], description = data['description'])
        if(new_article != None):
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404)
    
def article(request, article_id):

    if request.method == 'GET':
        article = Article.objects.filter(pk = article_id)
        return JsonResponse({
            "article" : serializers.serialize('json',article)
        })
  
    

