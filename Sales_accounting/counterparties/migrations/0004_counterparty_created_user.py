# Generated by Django 3.0.6 on 2020-06-05 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('counterparties', '0003_auto_20200529_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterparty',
            name='created_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counterpartyes', to='account.Profile'),
        ),
    ]
