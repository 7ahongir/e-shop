# Generated by Django 3.1.4 on 2020-12-21 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_status', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery_status',
            old_name='info',
            new_name='status',
        ),
    ]