# Generated by Django 3.1.4 on 2021-01-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_App', '0003_auto_20210108_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]