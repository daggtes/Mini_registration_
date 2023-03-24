from django.db import models
from datetime import date, timedelta

# Create your models here.


class HouseHoldProgram(models.Model):
    """Choice for household programs"""

    HOUSE_HOLD_PROGRAM_CHOICES = (
        ('Public Work', 'Public work'),
        ('Direct Support', 'Direct Support')
    )
    HouseHoldProgram = models.CharField(max_length=30, null=True, choices=HOUSE_HOLD_PROGRAM_CHOICES, blank=True)


class EducationLevel (models.Model):
    """Level Choice"""

    EDUCATION_LEVEL_CHOICES = (
        ('High School Graduate', 'High School Graduate'),
        ('Some College', 'Some College'),
        ('Associate Degree', 'Associate Degree'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('MBA, Masters', 'MBA, Masters'),
        ('Doctorate', 'Doctorate')
    )

    EductionLevel = models.CharField(max_length=30, blank=True, null=True,choices=EDUCATION_LEVEL_CHOICES)


class HealthStatus (models.Model):
    """Health level status choice"""

    HEALTH_STATUS_CHOICES= (
        ('Healthy', 'Healthy' ),
        ('Unhealthy', 'Unhealthy')
    ) 
    HealthStatus = models.CharField(max_length=30, blank= True, null=True, choices=HEALTH_STATUS_CHOICES)

class MartialStatus(models.Model):
    
    """Martial Status choice"""

    MARTIAL_STATUS_CHOICE = (
        ('Single', 'Single'),
        ('In a Relationship', 'In a Relationship'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed')
    )

    MartialStatus = models.CharField(max_length=30, blank=True, null=True, choices=MARTIAL_STATUS_CHOICE)

class BeneficiaryType(models.Model):
    """Choice for Beneficary"""

    BENEFICARY_CHOICES = (
        ('Primary Beneficiary', 'Primary Beneficiary'),
        ('Contingent Beneficiary', 'Contingent Beneficiary'),
        ('Residuary Beneficiary', 'Resiudary Beneficiary')
    )

    BeneficiaryType = models.CharField(max_length=64, blank=True, null=True, choices=BENEFICARY_CHOICES)

class HouseHold (models.Model):

    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)
    UpdatedDate = models.DateTimeField(auto_now=True, null=True)

    """Status choices """
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = ((Active_Status, 'Active'), (Inactive_Status, 'Inactive'),)
    
    Status = models.IntegerField(choices=STATUS_CHOICES, default= Active_Status, null=True, blank=True)
    HouseHoldIdNumber = models.CharField(max_length=25, null=True, blank=True)
    MaleMemberSize = models.IntegerField(null=True, blank=True)
    FemaleMemberSize = models.IntegerField(null=True, blank=True)
    NumberOfParticipatingMale = models.IntegerField(null=True, blank=True)
    NumberOfParticipatingFemale = models.IntegerField(null=True, blank=True)
    NumberOfMaleAbleBody = models.IntegerField(null=True, blank=True)
    NumberOfFemaleAbleBody = models.IntegerField(null=True, blank=True)
    RegistrationDate = models.DateField(null=True, blank=True)
    HouseholdProgram = models.ForeignKey(HouseHoldProgram, on_delete=models.CASCADE, null=True, blank=True)
    @property
    def CreatedBy(self):
        CreatedBy= self.pk
        return CreatedBy
    @property
    def UpdatedBy(self):
        UpdatedBy= self.pk
        return UpdatedBy
    

class Member (models.Model):
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)
    UpdatedDate = models.DateTimeField(auto_now=True, null=True)

    """Status choices """
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = ((Active_Status, 'Active'), (Inactive_Status, 'Inactive'),)

    Status = models.IntegerField(choices=STATUS_CHOICES, default= Active_Status, null=True, blank=True)
    HouseholdMemberIdNumber = models.CharField(max_length=64, null=True, blank=True)
    NationalMemberIdNumber = models.CharField(max_length=64, null=True, blank=True)
    FirstName = models.CharField(max_length=64, null=True, blank=True)
    FatherName = models.CharField(max_length=64, null=True, blank=True)
    GrandFatherName = models.CharField(max_length=64, null=True, blank=True)
    MotherFullName = models.CharField(max_length=64,null=True, blank=True)

    """Gender choice"""
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    DateOfBirth = models.DateField(null=True, blank=True)
    

    

    """Calculating the Age automatically"""
    
    @property
    def Age(self):
        Age = date.today().year - self.DateOfBirth.year
        return Age
    
    

    Beneficiarytype = models.ForeignKey(BeneficiaryType, on_delete=models.CASCADE, null=True, blank=True)
    RelationToHousehold = models.ForeignKey(HouseHold, on_delete= models.CASCADE, null=True, blank=True)
    RegistrationDate = models.DateField(null=True, blank=True)
    Educationlevel = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, null=True, blank=True)
    Healthstatus = models.ForeignKey(HealthStatus, on_delete=models.PROTECT, null=True, blank=True)
    Martialstatus = models.ForeignKey(MartialStatus, on_delete=models.CASCADE, null=True, blank=True)
    CreatedBy = models.CharField(null=True,max_length=64, blank=True)
    UpdatedBy = models.CharField(null=True, max_length=64, blank=True)


    @property
    def CreatedBy(self):
        CreatedBy = self.FirstName
        return CreatedBy
    
    @property
    def UpdatedBy(self):
        UpdatedBy = self.FirstName
        return UpdatedBy



