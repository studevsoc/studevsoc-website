from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Contact
        fields = ('name','email','subject','message')
