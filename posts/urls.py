from django.urls import path
import posts.views as view

urlpatterns = [
    path("", view.HomePageView.as_view(), name="home"),
    path("about/", view.AboutPageView.as_view(), name="about"),
]