# Generated by Django 3.2.9 on 2021-12-28 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_roster', '0005_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='attendances',
        ),
    ]