from rest_framework.routers import DefaultRouter
from .views import XodimlarViewSet

router = DefaultRouter()
router.register(r'xodimlar', XodimlarViewSet, basename='xodimlar')

urlpatterns = router.urls
