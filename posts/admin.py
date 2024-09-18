from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
        'published_at',
    )
    list_editable = ('is_published',)
    list_filter = ('is_published', 'published_at', 'created_at')
    search_fields = ('title', 'slug')
    ordering = ('is_published', 'published_at')
    date_hierarchy = 'published_at'
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
