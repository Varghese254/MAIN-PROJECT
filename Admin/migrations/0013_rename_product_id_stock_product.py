# Generated by Django 4.1.5 on 2023-02-03 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_rename_product_stock_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='product_id',
            new_name='product',
        ),
    ]
