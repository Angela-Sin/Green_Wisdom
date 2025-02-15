from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogPost
from .forms import BlogPostForm


class Posts(ListView):
    """ View all posts"""
    template_name = 'blog/posts.html'
    model = BlogPost
    context_object_name = 'posts'


class AddPost(LoginRequiredMixin, CreateView):
    template_name = 'blog/add_post.html'
    model = BlogPost
    form_class = BlogPostForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
