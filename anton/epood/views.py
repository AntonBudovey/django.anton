from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Offer, Comment, avatarka
from django.views.generic.base import View
from .form import CommentForm, RegisterUserForm, ChangeUserProfile

# Create your views here.


class Homepage(ListView):
    paginate_by = 3
    model = Offer
    template_name = "epood/main.html"
    context_object_name = "offer_list"


class offer_detail(DetailView):
    model = Offer
    template_name = "epood/detail.html"
    slug_url_kwarg = "offer_slug"


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "epood/login.html"

    def get_success_url(self):
        return reverse_lazy("mainpage")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "epood/register.html"
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        print(form)
        user = form.save()
        a = avatarka(user_avatar_id=user.pk)
        a.save()
        login(self.request, user)
        return redirect("mainpage")


def logout_user(request):
    logout(request)
    return redirect("mainpage")


def ProfileUser(request, user_id):
    form = ChangeUserProfile(request.POST, request.FILES)
    if request.POST:
        obj = avatarka.objects.get(user_avatar_id = user_id)
        obj.pict = request.FILES.get("pict")
        obj.save()
        return redirect("profile", user_id=user_id)
    else:
        form = ChangeUserProfile()
    return render(request, "epood/user_profile.html", {"user": User.objects.get(pk=user_id), "form": form})



class AddComment(LoginRequiredMixin, View):
    login_url = "/login"
    def post(self, request, pk, offer_slug):
        form = CommentForm(request.POST)
        form = form.save(commit=False,)
        form.offer_id = pk
        form.author_name = request.user.username
        form.author_pict = request.user.avatarka.pict
        form.save()
        return redirect("details", offer_slug=offer_slug)