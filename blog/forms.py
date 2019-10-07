from django import forms
from .models import Post, Comment, Tag, BlogType
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    cover = forms.ImageField(label='Select an Image')
    class Meta:
        model = Post
        fields = ('title', 'cover', 'content', 'slug', 'tags', 'blogtype')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class TagForm(forms.ModelForm):
    name = forms.CharField(max_length=32, label='Tag Name ')
    class Meta:
        model = Tag
        fields = ('name',)

class BlogTypeForm(forms.ModelForm):

    class Meta:
        model = BlogType
        fields = ('name',)
