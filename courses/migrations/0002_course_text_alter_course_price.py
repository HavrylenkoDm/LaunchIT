# Generated by Django 4.1.3 on 2022-11-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='text',
            field=models.TextField(default='default text'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=10),
        ),
    ]
