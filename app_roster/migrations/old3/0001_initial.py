# Generated by Django 3.2.9 on 2021-12-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.BigIntegerField()),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('tell', models.CharField(max_length=20)),
                ('sex',models.CharField(max_length=1)),
                ('contract', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('deleteFlag', models.BooleanField(default=False)),
                ('updateTime', models.DateField(null=False)),
                ('addTime', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='attendances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendanceId', models.BigIntegerField()),
                ('userId', models.BigIntegerField()),
                ('yearMonth', models.CharField(max_length=6)),
                ('day', models.CharField(max_length=2)),
                ('startTime', models.DateField()),
                ('dndDateTime', models.DateTimeField()),
                ('restStartTime', models.DateTimeField()),
                ('restEndTime', models.DateTimeField()),
                ('deleteFlag', models.BooleanField(default=False)),
                ('updateTime', models.DateField(null=False)),
                ('addTime', models.BooleanField(null=True)),
            ],
        ),
    ]