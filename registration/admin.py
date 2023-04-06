from django.contrib import admin
from .models import Member, EducationLevel, HouseHold, HealthStatus,HouseHoldProgram, MartialStatus, BeneficiaryType
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','CreatedDate','UpdatedDate','Status',
                    'HouseholdMemberIdNumber','NationalMemberIdNumber','FirstName','FatherName',
                    'GrandFatherName','MotherFullName','Gender','DateOfBirth','Age','Beneficiarytype',
                    'RelationToHousehold','RegistrationDate','Educationlevel','Healthstatus','Martialstatus',]
    

admin.site.register(EducationLevel)
admin.site.register(HouseHoldProgram)

@admin.register(HouseHold)
class HouseHoldAdmin(admin.ModelAdmin):
    list_display = ['id','CreatedDate','UpdatedDate','Status',
                    'HouseHoldIdNumber','MaleMemberSize','FemaleMemberSize',
                    'NumberOfParticipatingMale','NumberOfParticipatingFemale','NumberOfMaleAbleBody',
                    'NumberOfFemaleAbleBody','RegistrationDate','HouseholdProgram',]
admin.site.register(HealthStatus)
admin.site.register(MartialStatus)
admin.site.register(BeneficiaryType)

