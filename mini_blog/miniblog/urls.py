from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import ArticleViewSet, KeywordViewSet
from . import views



router = DefaultRouter()
router.register(r'keywords', KeywordViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('insert_article/', views.insert_article, name='insert_article'),
]