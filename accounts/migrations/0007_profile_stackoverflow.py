# Generated by Django 2.2.5 on 2019-10-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stackoverflow',
            field=models.URLField(blank=True, default='https://stackoverflow.com/users/0000000'),
        ),
    ]
