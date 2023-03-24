from registration.models import Member, EducationLevel, MartialStatus, HealthStatus, HouseHold, HouseHoldProgram
from .serializers import MemberSerializers, EducationLevelSerializers, HealthStatusSerializers, HouseHoldProgramSerializers, HouseHoldSerializers, MartialStatusSerializers
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

class EducationLevelViewSet(viewsets.ModelViewSet):
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializers

class MartialStatusViewSet(viewsets.ModelViewSet):
    queryset = MartialStatus.objects.all()
    serializer_class = MartialStatusSerializers

class HealthStatusViewSet(viewsets.ModelViewSet):
    queryset = HealthStatus.objects.all()
    serializer_class = HealthStatusSerializers

class HouseHoldViewSet(viewsets.ModelViewSet):
    queryset = HouseHold.objects.all()
    serializer_class = HouseHoldSerializers

class HouseHoldProgramViewSet(viewsets.ModelViewSet):
    queryset = HouseHoldProgram.objects.all()
    serializer_class = HouseHoldProgramSerializers

