# Generated by Django 2.0.3 on 2018-04-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hive',
            name='makes_honey',
            field=models.BooleanField(default=False),
        ),
    ]
