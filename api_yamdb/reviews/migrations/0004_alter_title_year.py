# Generated by Django 3.2 on 2023-02-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(null=True, verbose_name='Год создания'),
        ),
    ]