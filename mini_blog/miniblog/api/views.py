from rest_framework import viewsets
from ..models import Article, Keyword
from .serializers import ArticleSerializer, KeywordSerializer


class ArticleSerializer(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class KeywordSerializer(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer