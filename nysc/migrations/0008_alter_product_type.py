# Generated by Django 5.0 on 2024-04-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nysc', '0007_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('kakhi', 'kakhi'), ('vest', 'vest'), ('cap', 'cap')], max_length=20),
        ),
    ]
