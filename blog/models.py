from django.db import models
from django.utils import timezone
# Create your models here.


class Post (models.Model):  # クラス名は大文字ではじめます
    author = models.ForeignKey('auth.User')
    title = models.TextField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()  # データベースの値を更新するメソッド
        print(self.published_date)
    
    def __str__(self):
        return self.title

