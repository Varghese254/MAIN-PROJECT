# Generated by Django 4.1.5 on 2023-01-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_vstatus',
            field=models.IntegerField(default=0),
        ),
    ]