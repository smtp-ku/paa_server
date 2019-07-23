# Generated by Django 2.2.3 on 2019-07-23 01:12

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookback_period', models.IntegerField()),
                ('ticker_list', django_mysql.models.ListCharField(models.CharField(max_length=20), max_length=2200, size=100)),
                ('protection_degree', models.IntegerField()),
                ('time_flag', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InvestReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invest_date', models.DateTimeField()),
                ('invest_plan', django_mysql.models.JSONField(default=dict)),
                ('evaluate_date', models.DateTimeField()),
                ('evaluate_revenue', models.FloatField()),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measure.Scenario')),
            ],
        ),
    ]
