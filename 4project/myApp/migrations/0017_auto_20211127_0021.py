# Generated by Django 2.2.24 on 2021-11-26 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0016_post_senduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='senduser',
            new_name='user',
        ),
    ]
