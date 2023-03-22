from name_registration.models import New
from .serializers import NewSerializers
from rest_framework import viewsets


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializers