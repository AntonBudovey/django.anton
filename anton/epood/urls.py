from django.urls import path
from . import views

urlpatterns = [
    path("", views.Homepage.as_view(), name="mainpage"),
    path("offer/<slug:offer_slug>/", views.offer_detail.as_view(), name="details"),
    path("offer/<slug:offer_slug>/review/<int:pk>", views.AddComment.as_view(),)
]