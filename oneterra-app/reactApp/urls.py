from rest_framework import routers
from .api import AppSettingsViewSet


router = routers.DefaultRouter()
router.register('app_settings', AppSettingsViewSet, 'app_settings')

urlpatterns = router.urls