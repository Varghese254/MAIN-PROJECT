# Generated by Django 4.1.5 on 2023-01-27 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='product_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='subcategory',
            new_name='product_subcategory',
        ),
    ]
