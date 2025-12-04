from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

class About(models.Model):
    about = models.CharField(max_length=3000)

class Addpersonaldetail(models.Model):
    Nationality = models.CharField(max_length=150)
    State = models.CharField(max_length=150)
    District = models.CharField(max_length=150)
    DOB = models.DateField()
    Address = models.CharField(max_length=1000)
    Religion = models.CharField(max_length=150)
    Sex = models.CharField(max_length=150)

class Education(models.Model):
    University = models.CharField(max_length=100,null=True,blank=True)
    Institute = models.CharField(max_length=100,null=True,blank=True)
    CourseName = models.CharField(max_length=150)
    Duration = models.CharField(max_length=150)
    StartDate = models.DateField()
    EndDate = models.DateField()

class WorkExperience(models.Model):
    STATUS_CHOICES = (
        ('working', 'Working'),
        ('not_working', 'Not Working'),
    )

    Company = models.CharField(max_length=150, null=True, blank=True)
    Field = models.CharField(max_length=150, null=True, blank=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='working')
    Duration = models.CharField(max_length=150, null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)

class Crtification(models.Model):
    Course = models.CharField(max_length=150)
    Defnition = models.CharField(max_length=1500)

class Language(models.Model):
    language = models.CharField(max_length=150)

class SKILL(models.Model):
    skill = models.CharField(max_length=150)

class Contact(models.Model):
    FullName = models.CharField(max_length=200)
    Emailaddress = models.CharField(max_length=300)
    Subject = models.CharField(max_length=1000)
    Message = models.TextField()