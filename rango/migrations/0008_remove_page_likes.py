# Generated by Django 2.2.28 on 2023-02-05 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_remove_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
    ]
