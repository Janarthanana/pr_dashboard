# Generated by Django 3.0.3 on 2020-03-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0002_auto_20200303_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcreation',
            name='assignee',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
