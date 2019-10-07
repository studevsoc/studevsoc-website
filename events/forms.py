from django import forms
from .models import Event, EventCategory
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class EventForm(forms.ModelForm):
    about = forms.CharField(widget=CKEditorUploadingWidget())
    cover = forms.ImageField(label='Select an Image')
    class Meta:
        model = Event
        fields = ('name', 'cover', 'about','date', 'enddate', 'venue', 'slug', 'website', 'registration', 'eventtype',)

class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ('name',)
