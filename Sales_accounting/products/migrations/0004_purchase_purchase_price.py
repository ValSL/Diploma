# Generated by Django 3.0.6 on 2020-06-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_price',
            field=models.IntegerField(default=0),
        ),
    ]