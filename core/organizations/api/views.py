from organizations.models import Organization
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissons import IsOrganizationOwner
from .serializers import OrganizationSerializer


class OrganizationListCreateApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        "organisation_name",
        "organization_type",
        "country",
        "organization_url",
        "number_of_employees",
    ]


class OrganizationDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOrganizationOwner]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
