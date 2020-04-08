from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, default='name')
    netID = models.CharField(max_length=8, primary_key=True)
    interests = models.CharField(max_length=100)
    gradYear = models.IntegerField(null=True)
    courseWork = models.CharField(max_length=500, default='courseWork')
    projects = models.CharField(max_length=500, default='projects')
    experiences = models.CharField(max_length=500, default='experiences')

    def __str__(self):
        return "Student: " + str(self.netID)

class Internship(models.Model):
    netID = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    companyName = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    numberRating = models.IntegerField(null=True)
    projectDescription = models.CharField(max_length=500)
    companyReview = models.CharField(max_length=500)
    startDate = models.DateTimeField(auto_now=True)
    endDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Internship: " + str(self.companyName)

class Company(models.Model):
    companyName = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=500)
    rating = models.IntegerField(null=True)
    sponsorDate = models.DateTimeField(auto_now=True)

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

    def __str__(self):
        return "Student Group: " + str(self.name)

