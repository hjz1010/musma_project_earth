# Generated by Django 4.1 on 2022-08-23 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detections', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='equipment_state',
        ),
    ]