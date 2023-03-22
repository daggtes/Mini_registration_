from name_registration.api.viewsets import NewViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('New', NewViewSet)