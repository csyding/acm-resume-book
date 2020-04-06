from django.db import models

# Create your models here.
class Student(models.Model):
    netID = models.CharField(max_length=8, primary_key=True)
    resumeID = models.IntegerField(null=True)
    interests = models.CharField(max_length=100)
    
class Resume(models.Model):
    netID = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    resumeID = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    gradYear = models.IntegerField(null=True)
    courseWork = models.CharField(max_length=500)
    projects = models.CharField(max_length=500)
    experiences = models.CharField(max_length=500)

class Internship(models.Model):
    netID = models.ForeignKey(to='Student')
    companyName = models.ForeignKey(to='Company')
    numberRating = models.IntegerField(null=True)
    projectDescription = models.CharField(max_length=500)
    companyReview = models.CharField(max_length=500)
    startDate = models.DateTimeField(auto_now=True)
    endDate = models.DateTimeField(auto_now=True)

class Company(models.Model):
    companyName = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=500)
    rating = models.IntegerField(null=True)
    sponsorDate = models.DateTimeField(auto_now=True)

class Recruiter(models.Model):
    recruiterName = models.CharField(max_length=20, primary_key=True)
    companyName = models.ForeignKey(to='Company', on_delete=models.CASCADE)



def __str__(self):
    return "Netid is: " + str(self.netID)


class StudentGroup(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Student Group: " + str(self.name)

