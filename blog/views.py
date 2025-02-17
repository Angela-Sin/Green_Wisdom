from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
)


from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogPost
from .forms import BlogPostForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        posts = super().get_queryset()
        print("Retrieved posts:", posts)
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
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Post delete """
    model = BlogPost
    success_url = '/blog/posts/'

    def test_func(self):
        return self.request.user == self.get_object().author