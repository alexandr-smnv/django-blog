from django.contrib import admin

from contact.models import ContactModel, ContactLink, About, Social, ImageAbout


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ('name',)


class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1


@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]


admin.site.register(ContactLink)
admin.site.register(Social)
