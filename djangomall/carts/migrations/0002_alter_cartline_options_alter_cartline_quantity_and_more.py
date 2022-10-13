# Generated by Django 4.1.1 on 2022-10-11 03:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productvariant'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartline',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='cartline',
            name='quantity',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterUniqueTogether(
            name='cartline',
            unique_together={('cart', 'product_variant')},
        ),
    ]
