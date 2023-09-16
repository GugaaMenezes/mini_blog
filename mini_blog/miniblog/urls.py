from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import ArticleViewSet, KeywordViewSet
# from .api.views import KeywordViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'keywords', KeywordViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]