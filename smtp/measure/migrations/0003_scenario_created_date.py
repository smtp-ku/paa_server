# Generated by Django 2.2.3 on 2019-07-24 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0002_auto_20190724_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
