from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="epood/anton_main.html"), name="mainpage"),
    path("catalog", views.Homepage.as_view(), name="catalog"),
    path("offer/<slug:offer_slug>/", views.offer_detail.as_view(), name="details"),
    path("offer/<slug:offer_slug>/review/<int:pk>", views.AddComment.as_view()),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/<int:user_id>/", views.ProfileUser, name="profile"),
    path("about", TemplateView.as_view(template_name="epood/contacts_page.html"), name="about")
]