# Generated by Django 4.1.5 on 2023-01-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_photo', models.FileField(upload_to='UserDocs/')),
                ('product_des', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.subcategory')),
            ],
        ),
    ]