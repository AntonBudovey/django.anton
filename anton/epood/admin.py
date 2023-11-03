from django.contrib import admin
from .models import Offer, Comment

# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_name", "offer_description", "offer_price")
    search_fields = ("offer_name",)
    prepopulated_fields = {"slug": ("offer_name",)}
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "rating")

