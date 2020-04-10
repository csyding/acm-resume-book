from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, default='name')
    netID = models.CharField(max_length=8, primary_key=True)
    interests = models.CharField(max_length=100, blank=True, default='interests')
    gradYear = models.IntegerField(default=0)
    courseWork = models.CharField(max_length=500, blank=True, default='course')
    projects = models.CharField(max_length=500, blank=True, default='projects')
    experiences = models.CharField(max_length=500, blank=True, default='experiences')

    def __str__(self):
        return "Student: " + str(self.netID)

class Internship(models.Model):
    netID = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    companyName = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    numberRating = models.FloatField(null=True)
    projectDescription = models.CharField(max_length=500)
    companyReview = models.CharField(max_length=500)
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "Internship: " + str(self.companyName)

class Company(models.Model):
    companyName = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=500, blank=True)
    rating = models.FloatField(null=True)
    sponsorDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "Company: " + str(self.companyName)

class Recruiter(models.Model):
    recruiterName = models.CharField(max_length=20, primary_key=True)
    companyName = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    
    def __str__(self):
        return "Recruiter: " + str(self.recruiterName)

class StudentGroup(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=1000)

    members = models.ManyToManyField(Student)

    def __str__(self):
        return "Student Group: " + str(self.name)

