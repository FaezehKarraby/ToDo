# Generated by Django 3.2.8 on 2022-01-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
