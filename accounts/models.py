from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from django.utils import timezone

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    basefilename, file_extension= os.path.splitext(filename)
    timenow = timezone.now()
    return 'profile/{userid}/{basename}{time}{ext}'.format(userid=instance.user.id, basename=basefilename, time=timenow.strftime("%Y%m%d%H%M%S"), ext=file_extension)
ROLE = (
    (0, "Member"),
    (1, "Volunteer"),
    (2, "Team Lead"),
    (3, "Admin"),
    (4,"Editor"),
    (5,"Publisher"),
    (6,"EventManager"),
    (7,"Event+Publisher"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE, default=0)
    profile = models.ImageField(upload_to=user_directory_path, default='profile.png',help_text="Profile Picture")
    bio = models.TextField(max_length=500, blank=True, default="ND")
    work = models.CharField(max_length=30, blank=True, default="Student", help_text="eg:- Web Developer ,s/w Architect, s/m admin...etc")
    location = models.CharField(max_length=30, blank=True, default="ND", help_text="eg:- College Name, organization name ..etc")
    organization = models.CharField(max_length=100, blank=True, default="ND")
    chapter = models.ForeignKey('accounts.SDSChapter', on_delete = models.CASCADE, default=1 )
    linkedin = models.URLField(max_length=200, blank=True, default="https://www.linkedin.com/in/username/")
    github = models.URLField(max_length=200, blank=True, default="https://github.com/username")
    twitter = models.URLField(max_length=200, blank=True, default="https://twitter.com/username")
    facebook = models.URLField(max_length=200, blank=True, default="https://facebook.com/username")
    instagram = models.URLField(max_length=200, blank=True, default="https://www.instagram.com/user.name/")
    stackoverflow = models.URLField(max_length=200, blank=True, default="https://stackoverflow.com/users/0000000")
    private = models.BooleanField(default=False, help_text="<b>Make Your Profile Private</b>")
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class SDSChapter(models.Model):
    name = models.CharField(max_length=32, unique=True)
    location = models.CharField(max_length=30, blank=True, default="ND", help_text="eg:- College Name, organization name ..etc")
    class Meta:
        verbose_name_plural = "Chapter"
    def __str__(self):
        return self.name
