from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin

from . import models

# class WomenAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')
#     list_editable = ('is_published',)
#     list_filter = ('is_published', 'time_create')
#     prepopulated_fields = {'slug': ('title',)}
#     fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
#     # Поля только для чтения
#     readonly_fields = ('time_create', 'time_update', 'get_html_photo')
#     save_on_top = True
#
#     def get_html_photo(self, object):
#         if object.photo:
#             return mark_safe(f"<img src='{object.photo.url}' width=50>")
#
#     get_html_photo.short_description = 'Миниатюра'


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    inlines = [RecipeInline]


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
