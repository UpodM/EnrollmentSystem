# Generated by Django 5.0.6 on 2024-06-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('year_level', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'level',
            },
        ),
    ]