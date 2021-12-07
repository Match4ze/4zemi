# Generated by Django 2.2.24 on 2021-10-15 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_heart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heart',
            name='heart_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='heart_user', to='myApp.login'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='heart',
            name='login_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_user', to='myApp.login'),
        ),
    ]