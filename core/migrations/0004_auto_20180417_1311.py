# Generated by Django 2.0.4 on 2018-04-17 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180417_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityjournal',
            name='end',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='activityjournal',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='registry',
            name='end',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
