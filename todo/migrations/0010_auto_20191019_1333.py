# Generated by Django 2.2 on 2019-10-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20191019_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
