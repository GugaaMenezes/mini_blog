from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    type = models.IntegerField()
    content = models.TextField()
    status = models.IntegerField()
    keyword_set = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.title