# Generated by Django 2.1.7 on 2019-03-12 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2z', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Contact',
        ),
        migrations.AddField(
            model_name='customer',
            name='contact',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerEmail',
            field=models.CharField(max_length=30, verbose_name='Customer_Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerId',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Customer_ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerName',
            field=models.CharField(max_length=30, verbose_name='Customer_Name'),
        ),
    ]
