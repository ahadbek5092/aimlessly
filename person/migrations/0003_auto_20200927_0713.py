# Generated by Django 3.1 on 2020-09-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
