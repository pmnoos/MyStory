from django import forms
from .models import Chapter
from tinymce.widgets import TinyMCE

class ChapterForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=True)

    class Meta:
        model = Chapter
        fields = ['title', 'subtitle', 'content', 'cover_image', 'slug']  # Include 'slug'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'w3-input w3-border w3-round'})
        self.fields['subtitle'].widget.attrs.update({'class': 'w3-input w3-border w3-round'})
        self.fields['content'].widget.attrs.update({'class': 'w3-input w3-border w3-round'})
        self.fields['cover_image'].widget.attrs.update({'class': 'w3-input w3-border w3-round'})
        self.fields['slug'].widget.attrs.update({'class': 'w3-input w3-border w3-round'})  # Add styling for 'slug'



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w3-input', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w3-input', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w3-input', 'placeholder': 'Confirm Password'}))
