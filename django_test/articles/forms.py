from .models import Article
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

        widgets = {
            'title' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "Название статьи",
            }),

            'text' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : "Текст статьи",
                'cols' : "20",
                'rows' : "10",
            }),

        }


