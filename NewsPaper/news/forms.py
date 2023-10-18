from django import forms
from .models import Post


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = None

    class Meta:
        model = Post
        fields = [
            'heading',
            'text',
            'category',
            'author',
        ]
