from django.views.generic import ListView
from blog.models import BlogPost
from django.shortcuts import render


class Index(ListView):
    template_name = 'home/index.html'
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.all().order_by('-published_date')[:4]


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)
