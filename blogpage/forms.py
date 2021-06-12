from django.forms import ModelForm

from blogpage.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
