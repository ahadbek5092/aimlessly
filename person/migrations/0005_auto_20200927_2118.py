# Generated by Django 3.1 on 2020-09-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20200927_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genral',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='genral',
            name='url',
            field=models.IntegerField(),
        ),
    ]