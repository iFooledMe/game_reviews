# Generated by Django 3.1 on 2020-08-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_reviewsite'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='misc_tags',
            field=models.ManyToManyField(to='reviews.ReviewSite'),
        ),
    ]
