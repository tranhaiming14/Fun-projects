# Generated by Django 5.1.4 on 2025-01-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='academic',
            field=models.CharField(choices=[('F', 'F'), ('D', 'D'), ('C', 'C'), ('B', 'B'), ('A', 'A'), ('S', 'S')], default='F', max_length=1),
        ),
        migrations.AddField(
            model_name='day',
            name='economics',
            field=models.CharField(choices=[('F', 'F'), ('D', 'D'), ('C', 'C'), ('B', 'B'), ('A', 'A'), ('S', 'S')], default='F', max_length=1),
        ),
        migrations.AddField(
            model_name='day',
            name='sr',
            field=models.CharField(choices=[('F', 'F'), ('D', 'D'), ('C', 'C'), ('B', 'B'), ('A', 'A'), ('S', 'S')], default='F', max_length=1),
        ),
        migrations.AddField(
            model_name='day',
            name='workout',
            field=models.CharField(choices=[('F', 'F'), ('D', 'D'), ('C', 'C'), ('B', 'B'), ('A', 'A'), ('S', 'S')], default='F', max_length=1),
        ),
    ]
