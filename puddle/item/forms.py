from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={'class': 'input'}),
            'name': forms.TextInput(attrs={
                'class': 'input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'input'
            }),
            'price': forms.TextInput(attrs={
                'class': 'input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'input'
            })
        }
