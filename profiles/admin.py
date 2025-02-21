from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "truncated_bio", "image")
    search_fields = ("user__username", "bio")

    def truncated_bio(self, obj):
        if obj.bio and len(obj.bio) > 50:
            return f"{obj.bio[:50]}..."
        return obj.bio

    truncated_bio.short_description = "Bio"


admin.site.register(Profile, ProfileAdmin)
