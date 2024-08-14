from rest_framework.routers import DefaultRouter
from .views import RankViewSet, ProfileViewSet, DocumentViewSet, BankDetailViewSet, DeviceViewSet

router = DefaultRouter()
router.register(r'ranks', RankViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'bankdetails', BankDetailViewSet)
router.register(r'devices', DeviceViewSet)
