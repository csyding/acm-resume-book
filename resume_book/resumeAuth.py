from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser, User, Group
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from . import views

import logging
logger = logging.getLogger(__name__)

def userInGroup(user, group):
    return user.is_authenticated and user.groups.filter(name = group).exists()

def getUserHomepage(user):
    # Admin login shortcut :')
    if user.username == 'admin':
        return HttpResponseRedirect(reverse('resume_book:adminHome'))

    if userInGroup(user, 'Student'):
        return HttpResponseRedirect(reverse('resume_book:studentHome'))
    elif userInGroup(user, 'Recruiter'):
        return HttpResponseRedirect(reverse('resume_book:recruiterHome'))
    else:
        return HttpResponse('You\'re neither a recruiter or student?? who are you?')

def loginPage(request):
    """ GET request show login page if they're not logged in. Otherwise, redirect
        them to the correct homepage.
        POST requests authenticate the user and redirect them
    """
    if request.method == 'GET':
        current_user = request.user;
        if not current_user.is_authenticated:
            return render(request, 'resume_book/login.html')
        else:
            # User has already logged in
            return getUserHomepage(current_user);
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return HttpResponse('login failed, matching user does not exist.')
        else:
            login(request, user)

        return getUserHomepage(user)

def validEmail(username, email, user_type):
    """ Makes sure that the email has an @ character, and that it matches the
        username/netId if the user is a student
    """
    if '@' in email:
        split_email = email.split('@')
        if user_type == 'Student' and username == split_email[0] and split_email[1] == 'illinois.edu':
            return True
        elif user_type == 'Recruiter':
            return True
    return False

def validPassword(password, confirm_password):
    return password == confirm_password and len(password) > 8

def studentExists(netId):
    """ Checks if the student entry exists in our SQL database """
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM resume_book_student WHERE netid=%s',
            params=[netId]
            )

        row = cursor.fetchone()
        if row is not None:
            return True

    return False


def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated and not request.user.username == 'admin':
            return HttpResponse('You already have an account! <a href=\"/loginPage\">Click here to return to the homepage.</a>')

        context = {
            'admin' : request.user.is_authenticated
        }
        return render(request, 'resume_book/signup.html', context)
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        user_type = request.POST.get('userType', 'Student')

        if not validEmail(username, email, user_type):
            return HttpResponse("""Invalid email! If you\'re a student, 
                                your email has to be your @illinois.edu email and
                                your username has to match your netID!""")

        if not validPassword(password, confirm_password):
            return HttpResponse('Your passwords have to match and be longer than 8 characters!')

        # usertype
        if user_type != 'Student' and user_type != 'Recruiter':
            return HttpResponse('You\'re neither student nor recruiter... who are you?')

        # This creates the user in the database
        new_user = User.objects.create_user(username, email, password)

        # A user's Group determines their permissions
        if user_type == 'Student':
            new_user.groups.add(Group.objects.get(name='Student'))
        elif user_type == 'Recruiter':
            new_user.groups.add(Group.objects.get(name='Recruiter'))

        # Since they signed up, might as well log them in too
        if not request.user.username == 'admin':
            authenticated_user = authenticate(username=username, password=password)
            login(request, authenticated_user)

            if user_type == 'Student' and not studentExists(username):
                newRequest = HttpRequest()
                newRequest.POST['netID'] = username
                newRequest.user = authenticated_user
                views.addStudent(newRequest)
                    
            return getUserHomepage(authenticated_user)

        # But if you are just making an account on someone's behalf, don't log in to the new account
        else:
            return HttpResponse('Account successfully created. <a href=\"/adminHome\">Click here to return to the homepage.</a>')