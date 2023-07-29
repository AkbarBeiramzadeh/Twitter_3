from django import forms
from .models import Post, Comment


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class PostSearchForm(forms.Form):
    search = forms.CharField()
