from django.urls import path
from .views import Profiles, EditProfile


urlpatterns = [
    path("user/<pk>/", Profiles.as_view(), name="profile"),
    path("edit/<pk>/", EditProfile.as_view(), name="edit_profile")
]