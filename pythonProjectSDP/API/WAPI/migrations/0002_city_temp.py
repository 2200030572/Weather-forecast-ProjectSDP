# Generated by Django 4.2.4 on 2023-09-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='temp',
            field=models.IntegerField(null=True),
        ),
    ]