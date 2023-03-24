from registration.api.viewsets import MemberViewSet, EducationLevelViewSet, MartialStatusViewSet, HealthStatusViewSet, HouseHoldProgramViewSet, HouseHoldViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Member', MemberViewSet)
router.register('EducationLevel', EducationLevelViewSet)
router.register('HouseHoldProgram', HouseHoldProgramViewSet)
router.register('Health Status', HealthStatusViewSet)
router.register('HouseHold', HouseHoldViewSet)
router.register('Martial Status', MartialStatusViewSet)