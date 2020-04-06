from django.contrib import admin

# Register your models here.
from .models import Student, StudentGroup

admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Resume)
admin.site.register(Internship)
admin.site.register(Company)
admin.site.register(Recruiter)
