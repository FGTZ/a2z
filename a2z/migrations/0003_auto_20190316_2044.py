# Generated by Django 2.1.7 on 2019-03-17 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a2z', '0002_auto_20190311_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessories',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='customize',
            name='picture',
        ),
    ]
