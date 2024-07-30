from django import forms
from .models import Todo, Video

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'file']