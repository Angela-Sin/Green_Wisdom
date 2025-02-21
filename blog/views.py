from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView,
)

from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q

from .models import BlogPost, Comment, Like
from .forms import BlogPostForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        # Get comments for the post
        context['comments'] = Comment.objects.filter(post=post)
       
        # Ensure user is authenticated before checking likes
        user = self.request.user
        if user.is_authenticated:
            context['is_liked'] = Like.objects.filter(
                user=user, post=post
            ).exists()
        else:
            context['is_liked'] = False  # Default to False for anonymous users
        
        return context


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

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().author
      

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Post delete """
    model = BlogPost
    success_url = '/blog/posts/'

    def test_func(self):
        return self.request.user == self.get_object().author
    

class AddComment(LoginRequiredMixin, CreateView):
    """ View for adding comments """
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(BlogPost, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(BlogPost, pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.kwargs["pk"]})
    

class ToggleLike(LoginRequiredMixin, DetailView):
    """Toggle like for a post."""

    model = BlogPost

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        like, created = Like.objects.get_or_create(
            user=request.user, post=post
        )

        if not created:
            like.delete()

        return HttpResponseRedirect(reverse('post_detail', args=[post.id]))
