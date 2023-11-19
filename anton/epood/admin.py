from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Offer, Comment, avatarka
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "offer_description", "offer_price", "get_photo")
    search_fields = ("offer_name",)
    prepopulated_fields = {"slug": ("offer_name",)}
    def get_photo(self, object):
        return mark_safe(f"<img src='{object.offer_picture.url}' width=70>")

    get_photo.short_description = "Picture"

    readonly_fields = ("get_photo",)

    fields = ("offer_name", "slug", "offer_description", "offer_price", "offer_picture", "get_photo")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "rating")

class AvatarInline(admin.StackedInline):
    model = avatarka
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [AvatarInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)