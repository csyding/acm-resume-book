from django.urls import path

from . import views

# This is a namespace, and is used in the 'url' tag template in .html files, and also in reverse()
app_name = 'resume_book'

urlpatterns = [
    path('', views.index, name='index'),
    path('studentgroups/', views.studentGroups, name='studentGroups'),
    path('studentgroups/addgroup', views.addGroup, name='addGroup'),
    path('studentgroups/removegroup/<str:group_name>', views.removeGroup, name='removeGroup'),
]
