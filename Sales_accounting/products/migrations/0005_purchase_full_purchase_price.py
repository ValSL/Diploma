# Generated by Django 3.0.6 on 2020-06-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_purchase_purchase_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='full_purchase_price',
            field=models.IntegerField(default=0),
        ),
    ]
