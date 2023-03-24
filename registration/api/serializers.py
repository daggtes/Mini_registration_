from rest_framework import serializers
from registration.models import Member, EducationLevel, HealthStatus, HouseHold, HouseHoldProgram, MartialStatus

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            '__all__'
        )

        

class EducationLevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel

        fields = (
            'EductionLevel',
        )

class HealthStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthStatus

        fields = (
            'HealthStatus',
        )

class MartialStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = MartialStatus
        fields = (
            'MartialStatus',
        )

class HouseHoldProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = HouseHoldProgram
        fields = (
            'HouseHoldProgram',
        )

class HouseHoldSerializers(serializers.ModelSerializer):
    class Meta:
        model = HouseHold
        fields = ( '__all__')
