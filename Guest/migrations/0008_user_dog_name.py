# Generated by Django 4.1.5 on 2023-04-15 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_user_user_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dog_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]