# Generated by Django 4.1.5 on 2023-03-01 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_user_dog_licence'),
        ('Admin', '0016_product'),
        ('User', '0005_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.IntegerField(default=0)),
                ('payment_status', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.IntegerField(default=1)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.booking')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.product')),
            ],
        ),
    ]