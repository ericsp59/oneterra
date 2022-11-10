from .models import AppSettings
from rest_framework import viewsets, permissions
from .serializers import AppSettingsSerializer

class AppSettingsViewSet(viewsets.ModelViewSet):
    queryset = AppSettings.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppSettingsSerializer