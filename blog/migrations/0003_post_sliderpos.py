# Generated by Django 2.2.5 on 2019-10-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191006_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sliderpos',
            field=models.IntegerField(choices=[(2, 'None'), (0, 'First'), (1, 'Other')], default=2),
        ),
    ]