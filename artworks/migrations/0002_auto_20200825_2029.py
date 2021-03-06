# Generated by Django 3.0.5 on 2020-08-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('artworks', '0001_initial')]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(
                max_length=500, unique=True, verbose_name='Category slug'
            ),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.CharField(
                max_length=500, unique=True, verbose_name='Genre slug'
            ),
        ),
    ]
