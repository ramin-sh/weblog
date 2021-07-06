from django.db import models
from django.contrib.auth.models import User
from jalali_date import datetime2jalali,date2jalali
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,allow_unicode=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def get_jalali_date(self):
        return datetime2jalali(self.created_on)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80,null=True)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.name



