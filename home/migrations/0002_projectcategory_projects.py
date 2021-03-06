# Generated by Django 2.2.5 on 2019-10-05 11:25

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import home.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cover', models.ImageField(default='defaultevent.jpg', upload_to=home.models.user_directory_path)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('progress', models.IntegerField(choices=[(0, 'Scheduled'), (1, 'Ongoing / Under development'), (2, 'Completed')], default=0)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(help_text='WARNING : Use the same slug for while creating a BLOG Post about projects', max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ProjectCategory')),
                ('projectmanager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]
