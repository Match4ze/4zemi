# Generated by Django 2.2.24 on 2021-11-09 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_auto_20211015_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobby1',
            field=models.CharField(choices=[('スポーツ', 'スポーツ'), ('読書', '読書'), ('旅行', '旅行'), ('カメラ', 'カメラ'), ('ドラマ・映画鑑賞', 'ドラマ・映画鑑賞'), ('アイドル', 'アイドル'), ('アニメ', 'アニメ'), ('漫画', '漫画'), ('料理', '料理')], max_length=5),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='hobby2',
            field=models.CharField(blank=True, choices=[('スポーツ', 'スポーツ'), ('読書', '読書'), ('旅行', '旅行'), ('カメラ', 'カメラ'), ('ドラマ・映画鑑賞', 'ドラマ・映画鑑賞'), ('アイドル', 'アイドル'), ('アニメ', 'アニメ'), ('漫画', '漫画'), ('料理', '料理')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='hobby3',
            field=models.CharField(blank=True, choices=[('スポーツ', 'スポーツ'), ('読書', '読書'), ('旅行', '旅行'), ('カメラ', 'カメラ'), ('ドラマ・映画鑑賞', 'ドラマ・映画鑑賞'), ('アイドル', 'アイドル'), ('アニメ', 'アニメ'), ('漫画', '漫画'), ('料理', '料理')], max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='Friend_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_req', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Friend_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_req', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp.login')),
            ],
        ),
    ]
