from django.contrib import admin
from .models import *

admin.site.register(Contact)
admin.site.register(CommentPost)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
    list_filter = ('title',)
    search_fields = ('status',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryPage(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
