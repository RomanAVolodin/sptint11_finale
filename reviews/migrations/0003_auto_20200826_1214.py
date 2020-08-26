# Generated by Django 3.0.5 on 2020-08-26 12:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_auto_20200826_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name='Artwork rating',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='review', unique_together={('id', 'author')}
        ),
    ]
