
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('new/', views.create_post, name="new"),
    path('profile/<str:name>' , views.profile, name="profile"),
    path('follow/', views.follow, name="follow"),
    path('following', views.following, name="following"),
    path('change/<int:id>', views.change_post, name="change"),
]
