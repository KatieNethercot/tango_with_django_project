# Generated by Django 2.2.28 on 2023-02-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
