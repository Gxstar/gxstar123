# Generated by Django 3.0.4 on 2020-04-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='createTime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='article',
            name='updateTime',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]