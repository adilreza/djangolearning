# Generated by Django 3.0.8 on 2020-07-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mydata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Integer', models.IntegerField()),
                ('Text', models.TextField()),
                ('Character', models.CharField(max_length=200)),
            ],
        ),
    ]
