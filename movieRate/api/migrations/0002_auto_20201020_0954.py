# Generated by Django 3.1.2 on 2020-10-20 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='starts',
            new_name='stars',
        ),
    ]