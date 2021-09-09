# Generated by Django 2.2.24 on 2021-09-08 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='images/initial.jpeg', upload_to='images/')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('birth', models.CharField(max_length=8)),
                ('school_name', models.CharField(max_length=50)),
                ('school_grade', models.CharField(choices=[('1', '1年生'), ('2', '2年生'), ('3', '3年生'), ('4', '4年生'), ('大学院', '大学院生')], max_length=1)),
                ('sexuality', models.CharField(choices=[('男', '男'), ('女', '女'), ('その他', 'その他')], max_length=5)),
                ('insta_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('SNS_name1', models.CharField(blank=True, max_length=50, null=True)),
                ('SNS_ID1', models.CharField(blank=True, max_length=50, null=True)),
                ('SNS_name2', models.CharField(blank=True, max_length=50, null=True)),
                ('SNS_ID2', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
