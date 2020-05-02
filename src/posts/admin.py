from django.contrib import admin
from posts.models import Post, Category, Author

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'overview', 'timestamp', 'comment_count', 'author', 'thumbnail', 
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Author)