from django.contrib import admin

from apps.blog.models import Blog, Category, Comment

admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "enabled",
    )
