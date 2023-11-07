from django.contrib import admin
from .models import Offer, Comment, avatarka
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "offer_description", "offer_price")
    search_fields = ("offer_name",)
    prepopulated_fields = {"slug": ("offer_name",)}
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "rating")

class AvatarInline(admin.StackedInline):
    model = avatarka
    can_delete = False
    verbose_name_plural = "employee"


class UserAdmin(BaseUserAdmin):
    inlines = [AvatarInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)