from django.contrib import admin
from .models import Member, EducationLevel, HouseHold, HealthStatus,HouseHoldProgram, MartialStatus, BeneficiaryType
# Register your models here.

admin.site.register(Member)
admin.site.register(EducationLevel)
admin.site.register(HouseHoldProgram)
admin.site.register(HouseHold)
admin.site.register(HealthStatus)
admin.site.register(MartialStatus)
admin.site.register(BeneficiaryType)