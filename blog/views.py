from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView,
)


from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q

from .models import BlogPost
from .forms import BlogPostForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            posts = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(summary__icontains=query) |
                Q(content__icontains=query) |
                Q(category__icontains=query)
            )
        else:
            posts = self.model.objects.all()
        return posts


class PostDetail(DetailView):
    """ Post Detail Wiew"""

    template_name = "blog/post_detail.html"
    model = BlogPost
    context_object_name = "post"


class AddPost(LoginRequiredMixin, CreateView):
    template_name = "blog/add_post.html"
    model = BlogPost
    form_class = BlogPostForm
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit post"""
    template_name = 'blog/edit_post.html'
    model = BlogPost
    form_class = BlogPostForm
    success_url = '/blog/posts/'

    def test_func(self):
        return self.request.user == self.get_object().author
    

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Post delete """
    model = BlogPost
    success_url = '/blog/posts/'

    def test_func(self):
        return self.request.user == self.get_object().author