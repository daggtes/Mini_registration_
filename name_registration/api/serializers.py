from rest_framework import serializers
from name_registration.models import New

class NewSerializers(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('Name', 'lastname', 'age', 'number')