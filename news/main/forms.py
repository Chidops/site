from django import forms
from .models import *


#class AddPostForm(forms.Form):
#    title = forms.CharField(max_length=255, label='Заголовок')
#    slug = forms.SlugField(max_length=255, label='URL')
#    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Содержание')
#    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
#    is_published = forms.BooleanField(label='Опубликовано', initial=True, required=False)
#    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбранна')

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Выберите категорию'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
