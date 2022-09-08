from django.urls import path

from .api import views

urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", views.UserProfileCreateApiView.as_view(), name="register"),
    path(
        "",
        views.UserListApiView.as_view(),
        name="user_list_create_api",
    ),
    path(
        "profile/",
        views.UserProfileAPIView.as_view(),
        name="user_profile_api",
    ),
]
