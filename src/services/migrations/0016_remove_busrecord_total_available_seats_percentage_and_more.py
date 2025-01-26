# Generated by Django 4.2 on 2025-01-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_busrecord_total_available_seats_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busrecord',
            name='total_available_seats_percentage',
        ),
        migrations.AddField(
            model_name='busrecord',
            name='total_filled_seats_percentage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
