# Generated by Django 3.1.4 on 2020-12-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brend',
            name='logo',
            field=models.ImageField(default=True, max_length=200, upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default=True, max_length=200, upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=True, max_length=200, upload_to='static/img'),
        ),
    ]
