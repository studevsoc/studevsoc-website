# Generated by Django 2.2.5 on 2019-10-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='private',
            field=models.BooleanField(default=False, help_text='<b>Make Your Profile Private</b>'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='ND', help_text='eg:- College Name, organization name ..etc', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work',
            field=models.CharField(blank=True, default='Student', help_text='eg:- Web Developer ,s/w Architect, s/m admin...etc', max_length=30),
        ),
    ]
