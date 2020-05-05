"""
This file contains views that are private to each student. Things like views to edit their own profile, or their
own student groups.
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import os 
from neo4j.v1 import GraphDatabase, basic_auth

from .models import Student;
from . import resumeAuth
from . import views

import logging
logger = logging.getLogger('privateViews')

# neo4j driver GrapheneDB
graphenedb_url = os.environ.get("GRAPHENEDB_BOLT_URL")
graphenedb_user = os.environ.get("GRAPHENEDB_BOLT_USER")
graphenedb_pass = os.environ.get("GRAPHENEDB_BOLT_PASSWORD")
driver = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))

class UserCountError(Exception):
    """Raised when there are none or multiple users with the primary key found when we expect 1"""
    pass

def getStudentContext(netId):
    # Fetch student from SQL database
    fetched_students = Student.objects.raw(
            'SELECT * FROM resume_book_student WHERE netID = %s', 
            params=[netId]
            )
    if len(fetched_students) != 1:
        raise UserCountError(f"Got {len(fetched_students)} results for netID but expected exactly 1")
    student = fetched_students[0]

    # Fetch interests and skills from neo4j database
    session = driver.session()
    skills_neo4j = session.run(
            'MATCH (a:Student)-[:SkilledIn]->(v:Skill) WHERE a.netid={netid} RETURN v.value',
            netid=netId
        )
    skill_strings = [record["v.value"] for record in skills_neo4j]
    skill_csv = ', '.join(skill_strings)

    interests_neo4j = session.run(
            'MATCH (a:Student)-[:InterestedIn]->(v:Interest) WHERE a.netid={netid} RETURN v.value',
            netid=netId
        )
    interest_strings = [record["v.value"] for record in interests_neo4j]
    interest_csv = ', '.join(interest_strings)
    session.close()

    # Put it all together!
    context = {
        'student': student,
        'skills': skill_csv,
        'interests': interest_csv,
        'name_length': Student._meta.get_field('name').max_length,
        'netID_length': Student._meta.get_field('netID').max_length,
        'courseWork_length': Student._meta.get_field('courseWork').max_length,
        'projects_length': Student._meta.get_field('projects').max_length,
        'experiences_length': Student._meta.get_field('experiences').max_length
    }

    return context


def studentHome(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse('You have to be a student to view this page!')

    try:
        context = getStudentContext(request.user.username)
    except UserCountError:
        return HttpResponse('Something went wrong! There\'s none or multiple people with your netID which shouldn\'t be possible.')

    return render(request, 'resume_book/studentHome.html', context)


def getStudentProfile(request):
    try:
        context = getStudentContext(request.user.username)
    except UserCountError:
        return HttpResponse('Something went wrong! There\'s none or multiple people with your netID which shouldn\'t be possible.')

    return render(request, 'resume_book/editStudent.html', context)


def updateStudentProfile(request):
    if (request.user.username != request.POST.get('netID')):
        return HttpResponse('You\'re trying to change data for a user that\'s not you. Kinda Suspicious.')

    # delegate the work to the /addStudent url for now, but ignore the redirect
    ignored_redirect = views.addStudent(request)

    return HttpResponseRedirect(reverse('resume_book:studentHome'))

def editSelf(request):
    if not request.user.is_authenticated:
        return HttpResponse('You need to log in to view this page!')
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse('You have to be a student to view this page!')

    if request.method == 'GET':
        return getStudentProfile(request)
    elif request.method == 'POST':
        return updateStudentProfile(request)


def editGroups(request):
    if not request.user.is_authenticated:
        return HttpResponse('You need to log in to view this page!')

    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse('You have to be a student to view this page!')

