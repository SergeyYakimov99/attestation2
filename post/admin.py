from django.contrib import admin
from django.urls import reverse

from django.utils.html import format_html

from post.models import User, Post, Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'date_birth']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user_link', 'text', 'created_at']

    list_filter = ['created_at']

    def user_link(self, obj):
        user = obj.author
        url = reverse("admin:post_user_changelist") + str(user.pk)
        return format_html(f'<a href="{url}">{user}</a>')

    user_link.short_description = "Автор"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'description', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
