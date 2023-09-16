from django.shortcuts import render

def insert_article(request):
    return render(request, 'insert_article.html')