from django import forms
from .models import Post, Image, Video, PDF

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class PostVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video']
        widgets = {
            'video': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class PostPDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['pdf']
        widgets = {
            'pdf': forms.ClearableFileInput(attrs={'multiple': True}),
        }

