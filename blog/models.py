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
    (3, "Spam")
)

SLIDERPOS = {
    (0,"First"),
    (1,"Other"),
    (2,"None")
}


class BlogType(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    timenow = timezone.now()
    return 'cover/{userid}/{date}/{basename}{time}{ext}'.format(userid=instance.author.id, basename=basefilename, date=timenow.strftime("%Y%m%d"), time=timenow.strftime("%H%M%S"), ext=file_extension)

def user_directory_path_slider(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    timenow = timezone.now()
    return 'slider/{userid}/{date}/{basename}{time}{ext}'.format(userid=instance.author.id, basename=basefilename, date=timenow.strftime("%Y%m%d"), time=timenow.strftime("%H%M%S"), ext=file_extension)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    blogtype = models.ForeignKey('blog.BlogType', on_delete = models.CASCADE, )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, help_text='This will define layout of your url eg:studevsoc.com/blog/your-slug')
    tags = models.ManyToManyField(Tag)
    cover = models.ImageField(upload_to=user_directory_path, default='default.png')
    content = RichTextUploadingField()
    updated_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    feature = models.BooleanField(default=False, help_text="<b>This will Displayed on Home Page</b>")
    slider = models.BooleanField(default=False, help_text='Add To Blog Slider')
    sliderpos =  models.IntegerField(choices=SLIDERPOS, default=2)
    slidercover = models.ImageField(upload_to=user_directory_path_slider, default='default.png')

    class Meta:
        ordering = ['-updated_on']

    def publish(self):
        self.updated_on = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def get_page_count(self):
        count = self.posts.count()
        pages = count / 4
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 5

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 4)
        return range(1, count + 1)

    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name="comments")
    author = models. CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    comment_status = models.IntegerField(choices=STATUS, default=1)
    def approve(self):
        self.comment_status = 1
        self.save()
    def __str__(self):
        return self.text
