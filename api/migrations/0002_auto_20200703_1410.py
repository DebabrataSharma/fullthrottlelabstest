# Generated by Django 3.0.6 on 2020-07-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]
