# Generated by Django 2.2.24 on 2022-01-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_auto_20220103_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q1',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q10',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q2',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q3',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q4',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q5',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q6',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q7',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q8',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='q9',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
    ]
