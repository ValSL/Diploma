# Generated by Django 3.0.6 on 2020-05-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counterparties', '0002_auto_20200529_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterparty',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
