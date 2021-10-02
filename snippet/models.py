from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=False, unique=True)

    @classmethod
    def create(cls, title):
        try:
            tag = cls.objects.get(title=title)
            return tag
        except cls.DoesNotExist:
            tag = cls.objects.create(title=title)
            return tag

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.title


class Snippet(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey('Tag', blank=True, null=True,on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'snippet'
