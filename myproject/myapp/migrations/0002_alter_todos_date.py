# Generated by Django 4.0.3 on 2022-03-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
