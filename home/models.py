from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
import os

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Withdrawn"),
)

RESPONSE = (
    (0, "NOT RESPONDED"),
    (1, "RESPONDED"),
    (2, "SPAM"),
)

PROGRESS = (
    (0, "Scheduled"),
    (1, "Ongoing / Under development"),
    (2, "Completed"),
)

def user_directory_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    timenow = timezone.now()
    return 'projects/{userid}/{date}{basename}{time}{ext}'.format(userid=instance.projectmanager.id, basename=basefilename, date=timenow.strftime("%Y%m%d"), time=timenow.strftime("%H%M%S"), ext=file_extension)

class Jumbotron(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='jubtron_authors')
    introtitle = models.CharField(max_length=200, unique=True)
    introcontent = RichTextUploadingField()
    updated_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-updated_on']
    def publish(self):
        self.updated_on = timezone.now()
        self.save()

    def __str__(self):
        return self.introtitle

class ProjectCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)
    class Meta:
        verbose_name_plural = "Project Categories"
    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey('home.ProjectCategory', on_delete=models.CASCADE)
    projectmanager = models.ForeignKey(User, on_delete= models.CASCADE, related_name='project_manager')
    name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to=user_directory_path, default='defaultevent.jpg')
    description = RichTextUploadingField()
    updated_on = models.DateTimeField(blank=True, null=True)
    progress = models.IntegerField(choices=PROGRESS, default=0)
    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True, help_text='WARNING : Use the same slug for while creating a BLOG Post about projects')


    class Meta:
        ordering = ['-updated_on']

    def publish(self):
        self.updated_on = timezone.now()
        self.save()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sds_response = models.IntegerField(choices=RESPONSE, default=0)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "contact"

    def __str__(self):
        return self.name + "-" +  self.email
