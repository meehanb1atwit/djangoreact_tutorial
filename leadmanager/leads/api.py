from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = LeadSerializer

    # only return leads from given user
    def get_queryset(self):
        return self.request.user.leads.all()

    # Save lead owner when lead created
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
