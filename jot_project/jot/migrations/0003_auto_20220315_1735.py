# Generated by Django 2.2.26 on 2022-03-15 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jot', '0002_auto_20220314_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_average_rating',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
