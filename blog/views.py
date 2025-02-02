
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

 # new ------------------------
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            form = CommentForm(request.POST)

            if form.is_valid():
                # Save the form data to the database
                my_model = form.save(commit=False)
                
                my_model.blog_post = self.object  # Assign the foreign key
                
                my_model.save()

                return render(request, self.template_name, self.get_context_data())  


