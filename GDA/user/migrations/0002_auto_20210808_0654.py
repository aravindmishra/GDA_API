# Generated by Django 2.1.2 on 2021-08-08 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusmodel',
            old_name='staus',
            new_name='status',
        ),
    ]
