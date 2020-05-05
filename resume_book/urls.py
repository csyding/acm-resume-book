from django.urls import path, include

from . import views
from . import privateViews

# This is a namespace, and is used in the 'url' tag template in .html files, and also in reverse()
app_name = 'resume_book'

urlpatterns = [
    path('', views.index, name='index'),

    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutPage/', views.logoutPage, name='logoutPage'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),

    path('adminHome/', views.adminHome, name='adminHome'),
    
    path('studentHome/', privateViews.studentHome, name='studentHome'),
    path('recruiterHome/', views.recruiterHome, name='recruiterHome'),
    path('edit/self/', privateViews.editSelf, name='editSelf'),
    path('edit/groups/', privateViews.editGroups, name='editGroups'),

    path('studentgroups/', views.studentGroups, name='studentGroups'),
    path('studentgroups/addgroup', views.addGroup, name='addGroup'),
    path('studentgroups/addstudenttogroup', views.addStudentToGroup, name='addStudentToGroup'),
    path('studentgroups/removegroup/<str:group_name>', views.removeGroup, name='removeGroup'),
    path('companies/', views.companies, name='companies'),
    path('companies/addcompany', views.addCompany, name='addCompany'),
    path('companies/removecompany/<str:company_name>', views.removeCompany, name='removeCompany'),
    path('students/', views.students, name='students'),
    path('students/addStudent', views.addStudent, name='addStudent'),
    path('students/removeStudent/<str:student_netID>', views.removeStudent, name='removeStudent'),
    # path('students/searchNetID/<str:query>', views.searchNetID, name='searchNetID'),
    path('recruiters/', views.recruiters, name='recruiters'),
    path('recruiters/addRecruiter', views.addRecruiter, name='addRecruiter'),
    path('recruiters/removeRecruiter/<str:recruiter_name>', views.removeRecruiter, name='removeRecruiter'),
    path('internships/', views.internships, name='internships'),
    path('internships/addInternship', views.addInternship, name='addInternship'),
    path('internships/removeInternship/<str:internship_netID>', views.removeInternship, name='removeInternship'),

    path('interestSearch/', views.interestSearch, name='interestSearch'),
    path('skillSearch/', views.skillSearch, name='skillSearch')
]
