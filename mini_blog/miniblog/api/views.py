from rest_framework import viewsets
from ..models import Article, Keyword
from .serializers import ArticleSerializer, KeywordSerializer
from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class KeywordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer