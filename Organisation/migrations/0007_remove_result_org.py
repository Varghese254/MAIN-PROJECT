# Generated by Django 4.1.5 on 2023-04-17 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organisation', '0006_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='org',
        ),
    ]
