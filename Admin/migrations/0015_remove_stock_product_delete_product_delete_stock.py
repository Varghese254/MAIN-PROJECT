# Generated by Django 4.1.5 on 2023-03-01 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_delete_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
