from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category=models.CharField('分类',max_length=100)
    class Meta:
        verbose_name="博客分类"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.category
class Article(models.Model):
    title=models.CharField('标题',max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    body=models.TextField('正文')
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,verbose_name='分类',blank=True,null=True)
    class Meta:
        verbose_name="文章"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title