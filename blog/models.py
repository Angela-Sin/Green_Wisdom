from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from cloudinary_storage.storage import MediaCloudinaryStorage


POST_CATEGORIES = (
    ("tips", "Gardening Tips"),
    ("organic", "Organic Gardening"),
    ("seasonal", "Seasonal Gardening"),
    ("composting", "Composting"),
    ("pest_control", "Pest Control"),
    ("plant_care", "Plant Care"),
    ("harvesting", "Harvesting"),
    ("edible_leaves", "Edible Leaves"),
    ("flowers", "Flowers"),
    ("fruits", "Fruits"),
    ("root_tubers", "Root & Tubers"),
    ("bulbs_stems", "Bulbs & Stems"),
    ("vegetable_history", "History of Vegetables"),
)


class BlogPost(models.Model):
    """
    A model to create and manage blog posts for a vegetable gardening website
    """

    author = models.ForeignKey(
        User, related_name="blog_author", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    summary = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextField(max_length=20000, null=False, blank=False)
    featured_image = ResizedImageField(
        size=[800, None],
        storage=MediaCloudinaryStorage(),
        quality=75,
        upload_to="gardening_blog/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(
            max_length=50,
            choices=POST_CATEGORIES,
            default="tips"
    )
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """
    A model for user comments on a blog post
    """
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"


class Like(models.Model):
    """
    A model for user likes on a blog post
    """
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')  

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.title}"
