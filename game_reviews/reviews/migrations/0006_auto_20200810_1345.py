# Generated by Django 3.1 on 2020-08-10 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20200810_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='misc_tags',
            new_name='review_site',
        ),
    ]
