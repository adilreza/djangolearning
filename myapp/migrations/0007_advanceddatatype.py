# Generated by Django 3.0.8 on 2020-08-10 15:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_charlotteajaxtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedDataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('json_data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
