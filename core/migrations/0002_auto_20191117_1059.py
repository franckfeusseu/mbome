# Generated by Django 2.2.7 on 2019-11-17 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresse',
            name='tel',
            field=models.CharField(max_length=20),
        ),
    ]
