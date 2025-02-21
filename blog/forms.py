from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import BlogPost, POST_CATEGORIES, Comment


class BlogPostForm(forms.ModelForm):
    """
    Form to create and manage blog posts for a vegetable gardening website
    """

    class Meta:
        model = BlogPost
        fields = [
            "title",
            "summary",
            "content",
            "featured_image",
            "image_alt",
            "category",
        ]

        widgets = {
            "summary": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Write brief summary of the post"
                }
            ),
            "content": RichTextWidget(),
            "category": forms.Select(choices=POST_CATEGORIES),
        }

        labels = {
            "title": "Blog Title",
            "summary": "Post Summary",
            "content": "Blog Content",
            "featured_image": "Featured Image",
            "image_alt": "Image Description (for accessibility)",
            "category": "Post Category",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Add a comment...'
                }
            ),
        }
