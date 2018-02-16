from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # そのままだとTextfieldのデフォルトがtextareaの40colsのため
        # widgetsを使ってTextInputに変更
        widgets = {'title': forms.TextInput()}


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text')
