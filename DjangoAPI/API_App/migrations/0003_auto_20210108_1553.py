# Generated by Django 3.1.4 on 2021-01-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_App', '0002_auto_20210107_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=62),
        ),
    ]