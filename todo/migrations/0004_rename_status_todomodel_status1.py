# Generated by Django 3.2.8 on 2022-01-12 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todomodel_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='status',
            new_name='status1',
        ),
    ]