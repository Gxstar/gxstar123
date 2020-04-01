from django.contrib import admin
from blog.models import Category,Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','createTime','updateTime')

admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)