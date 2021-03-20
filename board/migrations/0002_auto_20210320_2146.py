# Generated by Django 3.1.7 on 2021-03-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='duty',
        ),
        migrations.AddField(
            model_name='advisor',
            name='degree',
            field=models.CharField(default='Prof. Dr. ', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
