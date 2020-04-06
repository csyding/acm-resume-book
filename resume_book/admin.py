from django.contrib import admin

# Register your models here.
from .models import Student, StudentGroup

admin.site.register(Student)
admin.site.register(StudentGroup)
