# Generated by Django 2.2.5 on 2019-11-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20191126_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance',
            name='color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='appliance',
            name='date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='appliance',
            name='dateSold',
            field=models.CharField(max_length=200),
        ),
    ]