from django.db import models

# Create your models here.
class Student(models.Model):
    netID = models.CharField(max_length=8, primary_key=True)
    resumeID = models.IntegerField(null=True)
    interests = models.CharField(max_length=100)

    def __str__(self):
        return "Netid is: " + str(self.netID)


