from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    image_thumbnail = ImageSpecField(source='image',
                          processors=[Thumbnail(300, 300)],
                          format='JPEG',
                          options={'quality': 60})

    #user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                         on_delete=models.CASCADE)
    # articles_article_like_users 테이블 생성
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                        related_name='like_articles')

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                         on_delete=models.CASCADE)
