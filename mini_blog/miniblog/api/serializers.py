from rest_framework import serializers
from ..models import Article, Keyword

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
        
class ArticleSerializer(serializers.ModelSerializer):
    keyword_set = KeywordSerializer(many=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        
    def create(self, validated_data):
        keyword_data = validated_data.pop('keyword_set', [])
        article = Article.objects.create(**validated_data)
        
        for keyword_info in keyword_data:
            keyword, created = Keyword.objects.get_or_create(name=keyword_info['name'])
            article.keyword_set.add(keyword)
            
        return article