from django.contrib import admin

# Register your models here.
from .models import Student, StudentGroup, Internship, Company, Recruiter

admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Internship)
admin.site.register(Company)
admin.site.register(Recruiter)
