# Generated by Django 2.1.2 on 2018-10-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('UUID', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('extension', models.CharField(max_length=100)),
            ],
        ),
    ]