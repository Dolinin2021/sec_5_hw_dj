# Generated by Django 4.0.3 on 2022-03-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_measurement_updated_at_alter_measurement_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
