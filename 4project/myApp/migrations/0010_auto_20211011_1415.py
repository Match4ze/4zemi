# Generated by Django 2.2.24 on 2021-10-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_friend_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend_list',
            name='friend_req',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='friend_request',
            name='friend_req',
            field=models.TextField(blank=True),
        ),
    ]
