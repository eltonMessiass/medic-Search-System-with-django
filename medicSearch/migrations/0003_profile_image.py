# Generated by Django 4.1.7 on 2023-03-29 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0002_city_dayweek_speciality_state_profile_favorites_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]