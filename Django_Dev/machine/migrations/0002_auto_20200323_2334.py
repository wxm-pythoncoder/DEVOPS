# Generated by Django 2.2 on 2020-03-23 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='password',
            field=models.CharField(default='123456', max_length=128, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='performance',
            name='username',
            field=models.CharField(default='root', max_length=128, verbose_name='账号'),
        ),
    ]
