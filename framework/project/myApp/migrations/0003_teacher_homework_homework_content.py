# Generated by Django 2.0 on 2020-04-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_homework_iscomplete'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_homework',
            name='homework_content',
            field=models.CharField(default='1', max_length=50),
        ),
    ]