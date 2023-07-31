# Generated by Django 4.1.5 on 2023-02-11 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0004_user_dog_licence'),
        ('Admin', '0014_delete_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date', models.DateField()),
                ('schedule_time', models.TimeField()),
                ('schedule_venue', models.CharField(max_length=50)),
                ('schedule_details', models.TextField(null=True)),
                ('schedule_poster', models.FileField(upload_to='OrgDocs/')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.organization')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]