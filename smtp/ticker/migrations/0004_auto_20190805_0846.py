# Generated by Django 2.2.3 on 2019-08-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0003_ticker_isbond'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='isEnabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='isBond',
            field=models.BooleanField(default=False),
        ),
    ]
