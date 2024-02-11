# Generated by Django 5.0 on 2024-02-08 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nysc', '0004_product_measurement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='measurement',
        ),
        migrations.AddField(
            model_name='measurement',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nysc.product'),
        ),
    ]
