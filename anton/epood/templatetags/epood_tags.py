from django import template
from epood.models import *
from django.db.models import *

register = template.Library()

@register.simple_tag()
def get_rating(offer):
    if offer.comment_set.exists():
        return round(offer.comment_set.aggregate(Sum("rating"))['rating__sum'] / offer.comment_set.count(), 1)
    return "no rating"

