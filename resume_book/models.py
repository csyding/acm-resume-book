from django.db import models

# Create your models here.
class Student(models.Model):
    netID = models.CharField(max_length=8, primary_key=True)
    resumeID = models.IntegerField(null=True)
    interests = models.CharField(max_length=100)

    def __str__(self):
        return "Netid is: " + str(self.netID)


class StudentGroup(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Student Group: " + str(self.name)

