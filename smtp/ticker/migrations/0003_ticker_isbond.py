# Generated by Django 2.2.3 on 2019-08-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0002_auto_20190716_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='isBond',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
