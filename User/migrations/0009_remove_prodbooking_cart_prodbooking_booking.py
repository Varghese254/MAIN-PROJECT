# Generated by Django 4.1.5 on 2023-03-21 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_prodbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodbooking',
            name='cart',
        ),
        migrations.AddField(
            model_name='prodbooking',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.booking'),
        ),
    ]
