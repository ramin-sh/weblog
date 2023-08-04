from django.db.models import fields
from django.forms import widgets
from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['blog_post'].initial = Comment.objects.get(id=)

    class Meta:
        model = Comment
        fields = ('name', 'text')
        help_tesxts={'name':'نام'}
        labels = {'name':'نام','text':'نظر'}

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = '__all__'