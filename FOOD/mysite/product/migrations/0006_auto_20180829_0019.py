# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='product.Product_Details'),
        ),
    ]
