from django import forms
from django.contrib.auth import get_user_model
from .models import Post







class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text','author']

    text = forms.CharField(
        required=True,
        label='Text',
        widget=forms.Textarea
    )

    author = forms.CharField(
        required=True,
        label='Autor',
        widget=forms.TextInput
    )
    # creator = forms.CharField(widget=forms.HiddenInput)


    # def save(self):
    #     print(self.cleaned_data)
    #     post = Post(self.cleaned_data)
    #     post.save()
    