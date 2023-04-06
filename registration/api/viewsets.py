from registration.models import Member, EducationLevel, MartialStatus, HealthStatus, HouseHold, HouseHoldProgram
from .serializers import MemberSerializers, EducationLevelSerializers, HealthStatusSerializers, HouseHoldProgramSerializers, HouseHoldSerializers, MartialStatusSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(Created_by = self.request.user)

    def perform_update(self, serializer):
        serializer.save(Updated_by = self.request.user)

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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(Created_by = self.request.user)

    def perform_update(self, serializer):
        serializer.save(Updated_by = self.request.user)

class HouseHoldProgramViewSet(viewsets.ModelViewSet):
    queryset = HouseHoldProgram.objects.all()
    serializer_class = HouseHoldProgramSerializers

