# Generated by Django 2.1.3 on 2019-01-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20181223_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='轮播图片'),
        ),
    ]
