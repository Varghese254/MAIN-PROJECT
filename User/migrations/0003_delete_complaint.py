# Generated by Django 4.1.5 on 2023-02-05 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_rename_complaint_complaint_organisation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Complaint',
        ),
    ]
