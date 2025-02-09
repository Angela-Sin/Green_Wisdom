from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "published_date",
        "updated_date",
        "featured_image",
        "summary",
    )
    search_fields = ("title", "summary", "content")
    list_filter = ("category", "published_date")
    ordering = ("-published_date",)