# Generated by Django 2.2.7 on 2019-11-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=140)),
                ('prenom', models.CharField(max_length=140)),
                ('genre', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('pays', models.CharField(max_length=140)),
                ('region', models.CharField(max_length=140)),
                ('ville', models.CharField(max_length=140)),
                ('profession', models.CharField(max_length=140)),
                ('tel', models.PositiveIntegerField()),
            ],
        ),
    ]
