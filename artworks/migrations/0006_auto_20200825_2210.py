# Generated by Django 3.0.5 on 2020-08-25 22:10

import artworks.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('artworks', '0005_auto_20200825_2146')]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    artworks.models.max_value_current_year,
                ],
                verbose_name='Artwork rating',
            ),
        )
    ]