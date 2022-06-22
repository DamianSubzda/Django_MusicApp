from django.forms import ModelForm, TextInput
from main.models import PlayList


class PlayListForm(ModelForm):
    class Meta:
        model = PlayList
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
            })
        }