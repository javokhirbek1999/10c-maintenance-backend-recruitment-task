# Generated by Django 4.0.1 on 2022-01-15 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='matching_projects',
        ),
    ]