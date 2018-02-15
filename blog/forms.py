from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # そのままだとTextfieldのデフォルトがtextareaの40colsのため
        # widgetsを使ってTextInputに変更
        widgets = {'title': forms.TextInput()}
