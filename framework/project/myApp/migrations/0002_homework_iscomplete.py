# Generated by Django 2.0 on 2020-04-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='isComplete',
            field=models.BooleanField(default=False),
        ),
    ]