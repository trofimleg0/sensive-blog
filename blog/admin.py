from django.contrib import admin
from blog.models import Post, Tag, Comment


admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "published_at",
    )
    raw_id_fields = ("likes", "tags")


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "author",
        "published_at",
    )
    raw_id_fields = ("author",)
