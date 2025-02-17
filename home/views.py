from django.views.generic import ListView
from blog.models import BlogPost


class Index(ListView):
    template_name = 'home/index.html'
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
         return self.model.objects.all().order_by('-published_date')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = "Welcome to the Gardening Blog!"
        return context