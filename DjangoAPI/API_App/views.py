from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def articles(request):

    if request.method == 'GET':
        return JsonResponse({
            "articles" : "retuned all articles"
        })
    elif request.method == 'POST':
        return JsonResponse({
            "articles" : "article inserted"
        })
    
def article(request, article_id):

    if request.method == 'GET':
        return JsonResponse({
            "article found :" : article_id
        })
    elif request.method == 'PUT':
        return JsonResponse({
            "article updated :" : article_id
        })
    elif request.method == 'DELETE':
        return JsonResponse({
            "article deleted :" : article_id
        })
    

