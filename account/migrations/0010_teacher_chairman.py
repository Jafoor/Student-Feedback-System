# Generated by Django 3.0.7 on 2022-01-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='chairman',
            field=models.BooleanField(default=False),
        ),
    ]