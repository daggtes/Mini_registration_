from rest_framework import serializers
from registration.models import Member, EducationLevel, HealthStatus, HouseHold, HouseHoldProgram, MartialStatus

class MemberSerializers(serializers.ModelSerializer):
    Created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    Updated_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    class Meta:
        model = Member
        fields = (
            'id','CreatedDate','UpdatedDate','Status',
            'HouseholdMemberIdNumber','NationalMemberIdNumber','FirstName','FatherName',
            'GrandFatherName','MotherFullName','Gender','DateOfBirth','Age','Beneficiarytype',
            'RelationToHousehold','RegistrationDate','Educationlevel','Healthstatus','Martialstatus','Created_by' ,'Updated_by',
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
    Created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    Updated_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    class Meta:
        model = HouseHold
        fields = (  'id','CreatedDate','UpdatedDate','Status',
                'HouseHoldIdNumber','MaleMemberSize','FemaleMemberSize',
                'NumberOfParticipatingMale','NumberOfParticipatingFemale','NumberOfMaleAbleBody',
                'NumberOfFemaleAbleBody','RegistrationDate','HouseholdProgram','Created_by', 'Updated_by',)

