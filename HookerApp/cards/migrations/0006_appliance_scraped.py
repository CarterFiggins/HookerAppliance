# Generated by Django 2.2.5 on 2019-12-23 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20191126_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliance',
            name='scraped',
            field=models.BooleanField(default=False),
        ),
    ]
