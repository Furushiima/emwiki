# Generated by Django 2.2.20 on 2021-06-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]
