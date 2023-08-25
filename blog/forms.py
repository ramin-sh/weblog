from django.db.models import fields
from django.forms import widgets
from .models import Comment, Post
from django import forms
from django.forms import Textarea

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

#new------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {'title':'موضوع','author':'نویسنده','content':'محتوا','status':'وضعیت'}
        # widgets = { "content": Textarea(attrs={"cols": 150, "rows": 20}),}
