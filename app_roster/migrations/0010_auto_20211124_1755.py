# Generated by Django 3.2.5 on 2021-11-24 08:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_roster', '0009_rename_endtime_attendance_enddatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='deleteFlag',
            field=models.IntegerField(default=1, verbose_name='deleteFlag'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='addTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='updateTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='addTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleteFlag',
            field=models.IntegerField(default=1, verbose_name='deleteFlag'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]