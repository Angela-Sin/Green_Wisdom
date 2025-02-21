from django.urls import path
from .views import (
    AddPost,
    Posts,
    PostDetail,
    PostDelete,
    EditPost,
    AddComment,
    ToggleLike,
)

urlpatterns = [
    path("", Posts.as_view(), name="blog_home"),
    path("add/", AddPost.as_view(), name="add_post"),
    path("posts/", Posts.as_view(), name="posts"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:pk>/", PostDelete.as_view(), name="post_delete"),
    path("edit/<slug:pk>/", EditPost.as_view(), name="edit_post"),
    path('post/<int:pk>/comment/', AddComment.as_view(), name='add_comment'),
    path('post/<int:pk>/like/', ToggleLike.as_view(), name='toggle_like'),
]
