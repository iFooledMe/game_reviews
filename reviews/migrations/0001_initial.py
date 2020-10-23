# Generated by Django 3.1.2 on 2020-10-23 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0002_auto_20201023_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('site_short_name', models.CharField(max_length=50)),
                ('site_url', models.URLField(blank=True, max_length=255, null=True)),
                ('site_url_name', models.CharField(blank=True, max_length=50, null=True)),
                ('logo_img', models.ImageField(blank=True, max_length=255, null=True, upload_to='review_sites/logo_images/')),
                ('show_logo_img', models.BooleanField(default=False)),
                ('logo_icon', models.CharField(blank=True, max_length=50, null=True)),
                ('show_logo_icon', models.BooleanField(default=False)),
                ('max_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('review_date', models.DateField(blank=True, null=True)),
                ('review_url', models.URLField(blank=True, max_length=255, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('max_score', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('short_quote', models.TextField(blank=True, max_length=500, null=True)),
                ('long_quote', models.TextField(blank=True, max_length=10000, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='reviews/review_images/')),
                ('show_logo_img', models.BooleanField(default=False)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.game')),
                ('review_site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.reviewsite')),
            ],
        ),
    ]
