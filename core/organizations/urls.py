from django.urls import path
from .api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(
    r"organizations", views.OrganizationListCreateApiView, basename="organizations"
)

urlpatterns = [
    path(
        "",
        views.OrganizationListCreateApiView.as_view(),
        name="organizations_list_create_api",
    ),
    path(
        "<int:pk>",
        views.OrganizationDetailAPIView.as_view(),
        name="organizations_detail_api",
    ),
]
