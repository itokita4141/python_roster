# Generated by Django 3.2.5 on 2021-11-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_roster', '0006_auto_20211123_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='day',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
