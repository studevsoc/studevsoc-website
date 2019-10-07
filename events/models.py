from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
import os

STATUS = (
    (0,"Scheduled"),
    (1,"Draft"),
    (2,"Withdrawn")
)

def user_directory_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    timenow = timezone.now()
    return 'events/{userid}/{date}{basename}{time}{ext}'.format(userid=instance.scheduler.id, basename=basefilename, date=timenow.strftime("%Y%m%d"), time=timenow.strftime("%H%M%S"), ext=file_extension)

class EventCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Event(models.Model):
    scheduler = models.ForeignKey(User, on_delete= models.CASCADE, related_name="events")
    eventtype = models.ForeignKey('events.EventCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(max_length=200)
    maplink = models.URLField(max_length=200, blank=True, default="#")
    cover = models.ImageField(upload_to=user_directory_path, default='defaultevent.jpg')
    about = RichTextUploadingField()
    scheduled_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=1)
    slug = models.SlugField(max_length=200, unique=True, help_text='WARNING : Use the same slug for while creating a BLOG Post about events')
    website = models.URLField(max_length=200, blank=True, default="#")
    registration = models.URLField(max_length=200, blank=True, default="#")

    class Meta:
        ordering = ['-date']

    def publish(self):
        self.scheduled_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name
