# Generated by Django 3.1 on 2020-10-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200827_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hide_info',
            field=models.BooleanField(default=False),
        ),
    ]
