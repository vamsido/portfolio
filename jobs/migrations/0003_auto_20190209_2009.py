# Generated by Django 2.0.2 on 2019-02-09 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190209_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imageff',
            new_name='image',
        ),
    ]
