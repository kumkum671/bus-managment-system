# Generated by Django 4.2 on 2024-12-28 11:35

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_routefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routefile',
            name='file',
            field=models.FileField(upload_to=services.models.rename_uploaded_file),
        ),
    ]