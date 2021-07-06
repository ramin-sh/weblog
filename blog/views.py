
from .forms import CommentForm
from django.views import generic
from .models import Post,Comment
from django.shortcuts import render
# from django.core.paginator  import Paginator


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 4#new
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

