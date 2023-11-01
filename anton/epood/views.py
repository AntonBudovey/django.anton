from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Offer, Comment
from django.views.generic.base import View
from .form import CommentForm

# Create your views here.


class Homepage(ListView):
    model = Offer
    template_name = "epood/main.html"
    context_object_name = "offer_list"

class offer_detail(DetailView):
    model = Offer
    template_name = "epood/detail.html"
    slug_url_kwarg = "offer_slug"


"""def offer_detail(request, offer_slug):
    return render(request, "epood/detail.html", {'offer': Offer.objects.get(slug=offer_slug)})"""


class AddComment(View):
    def post(self, request, pk, offer_slug):
        form = CommentForm(request.POST)
        form = form.save(commit=False,)
        form.offer_id = pk
        form.save()
        return redirect("details", offer_slug=offer_slug)