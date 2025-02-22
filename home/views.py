from django.views.generic import ListView
from blog.models import BlogPost


class Index(ListView):
    template_name = 'home/index.html'
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.all().order_by('-published_date')[:4]


