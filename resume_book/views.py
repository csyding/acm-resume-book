from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Q
from django.db import connection

from .models import StudentGroup;
from .models import Company;
from .models import Internship;
from .models import Recruiter;
from .models import Student;

# Authorization of our app's users
from django.contrib.auth.models import AnonymousUser, User, Group
from django.contrib.auth import authenticate, login, logout

from . import resumeAuth

import os 
from neo4j.v1 import GraphDatabase, basic_auth

import datetime

import logging
logger = logging.getLogger(__name__)

graphenedb_url = os.environ.get("GRAPHENEDB_BOLT_URL")
graphenedb_user = os.environ.get("GRAPHENEDB_BOLT_USER")
graphenedb_pass = os.environ.get("GRAPHENEDB_BOLT_PASSWORD")

driver = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))

NOT_AUTHENTICATED_RESPONSE = 'You are not authorized to view this page! <a href=\"/logoutPage\">Click here to switch users.</a>'

# Create your views here.
def index(request):
    return render(request, 'resume_book/index.html')

def logoutPage(request):
    logout(request);
    return HttpResponseRedirect(reverse('resume_book:loginPage'))

def loginPage(request):
    return resumeAuth.loginPage(request)

def signup(request):
    return resumeAuth.signup(request)

def adminHome(request):
    if not request.user.username == 'admin':
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    return render(request, 'resume_book/adminHome.html')

def studentHome(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    return render(request, 'resume_book/studentHome.html')

def recruiterHome(request):
    if not resumeAuth.userInGroup(request.user, 'Recruiter'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    return render(request, 'resume_book/recruiterHome.html')

def studentGroups(request):
    if not request.user.is_authenticated:
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    name_query = request.GET.get('name', '')

    sql_query_string = 'SELECT * FROM resume_book_studentgroup'

    if name_query:
        sql_query_string += ' WHERE name=' + name_query

    queried_studentGroups = StudentGroup.objects.raw(sql_query_string)

    context = {
            'queried_studentGroups': queried_studentGroups,
            'name_length': StudentGroup._meta.get_field('name').max_length,
            'desc_length': StudentGroup._meta.get_field('description').max_length
            }
    
    if request.user.username == 'admin':
        return render(request, 'resume_book/studentGroups.html', context)
    elif resumeAuth.userInGroup(request.user, 'Recruiter'):
        return render(request, 'resume_book/studentGroups-recruiter.html', context)
    else:
        return render(request, 'resume_book/studentGroups-student.html', context)

def addGroup(request):
    if not request.user.username == 'admin':
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    groupName = request.POST.get('name')
    groupDescription = request.POST.get('description')
    groupDescription.replace("'", "\\'")

    cursor = connection.cursor()
    q = 'SELECT * FROM resume_book_studentgroup WHERE name = \"{}\"'.format(groupName)
    cursor.execute(q)
    rows = cursor.fetchall()

    if rows:
        existingGroup = rows[0]
        sql_query_string = 'UPDATE resume_book_studentgroup \n SET '
        sql_query_string += 'description = \"{}\" \n'.format(groupDescription if groupDescription else existingGroup[1])
        sql_query_string += 'WHERE name = \"{}\"; '.format(groupName)
        cursor.execute(sql_query_string)

    else:
        sql_query_string = """INSERT INTO resume_book_studentgroup (name, description) \n 
                                VALUES (\"{}\", \"{}\");
                                """.format(groupName, groupDescription)
        cursor.execute(sql_query_string)


    return HttpResponseRedirect(reverse('resume_book:studentGroups'))

def addStudentToGroup(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    groupName = request.POST.get('name')
    netID = request.POST.get('netID')

    cursor = connection.cursor()
    q1 = 'SELECT * FROM resume_book_studentgroup WHERE name = \"{}\"'.format(groupName)
    cursor.execute(q1)
    rows1 = cursor.fetchall()

    q2 = 'SELECT * FROM resume_book_student WHERE netID = \"{}\"'.format(netID)
    cursor.execute(q2)
    rows2 = cursor.fetchall()

    if rows1 and rows2:
        existingGroup = rows1[0]
        existingStudent = rows2[0]
        print(existingGroup)
        print(existingStudent)
        sql_query_string = """INSERT INTO resume_book_studentgroup_members (studentgroup_id, student_id) \n 
                                VALUES (\"{}\", \"{}\");
                                """.format(existingGroup[0], existingStudent[0])
        cursor.execute(sql_query_string)

    return HttpResponseRedirect(reverse('resume_book:studentGroups'))


def removeGroup(request, group_name):
    if not request.user.username == 'admin':
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_studentgroup WHERE name=\"{}\"'.format(group_name))

    return HttpResponseRedirect(reverse('resume_book:studentGroups'))

def companies(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    name_query = request.GET.get('companyName', '')
    equalitySymbol = request.GET.get('equality', '')
    rating_query = request.GET.get('rating', '')
    sql_query_string = 'SELECT * FROM resume_book_company'

    compounds = 0
    if name_query:
        sql_query_string += ' WHERE companyName = \"' + name_query + '\"'
        compounds += 1

    if rating_query:
        if compounds > 0: 
            sql_query_string += ' AND '
        else:
            sql_query_string += ' WHERE '
        sql_query_string += 'numberRating ' + equalitySymbol + ' ' + rating_query

    queried_companies = Company.objects.raw(sql_query_string)        

    context = {
            'queried_companies': queried_companies,
            'name_length': Company._meta.get_field('companyName').max_length,
            'desc_length': Company._meta.get_field('description').max_length,
            'rating': Company._meta.get_field('rating'),
            'sponsorDate': Company._meta.get_field('sponsorDate').max_length,

            }
    if request.user.username == 'admin':
        return render(request, 'resume_book/companies.html', context)
    else:
        return render(request, 'resume_book/companies-noauth.html', context)

def addCompany(request):
    if not request.user.username == 'admin':
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    companyName = request.POST.get('companyName')
    companyDescription = request.POST.get('description', False)
    companyRating = request.POST.get('rating', False)
    companySponsorDate = request.POST.get('sponsorDate')
    companyDescription.replace("'", "\\'")

    cursor = connection.cursor()
    q = 'SELECT * FROM resume_book_company WHERE companyName = \"{}\"'.format(companyName)
    cursor.execute(q)
    rows = cursor.fetchall()
    if rows:
        existingCompany = rows[0]
        sql_query_string = 'UPDATE resume_book_company \n SET '
        sql_query_string += 'description = \"{}\", '.format(companyDescription if companyDescription else existingCompany[1])
        sql_query_string += 'rating = {}, '.format(companyRating if companyRating else existingCompany[2])
        sql_query_string += 'sponsorDate = \'{}\' \n'.format(companySponsorDate if companySponsorDate else existingCompany[3])
        sql_query_string += 'WHERE companyName = \"{}\"; '.format(companyName)
        cursor.execute(sql_query_string)

    else:
        sql_query_string = """INSERT INTO resume_book_company (companyName, description, rating, sponsorDate) \n 
                                VALUES (\"{}\", \"{}\", {}, \"{}\");
                                """.format(companyName, companyDescription, companyRating, companySponsorDate)
        cursor.execute(sql_query_string)

    return HttpResponseRedirect(reverse('resume_book:companies'))

def removeCompany(request, company_name):
    if not request.user.username == 'admin':
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_company WHERE companyName=\"{}\"'.format(company_name))
    return HttpResponseRedirect(reverse('resume_book:companies'))


def internships(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    companyName_query = request.GET.get('companyName', '')
    equality_symbol = request.GET.get('equality', '')
    numberRating_query = request.GET.get('numberRating', '')
    cursor = connection.cursor()
    sql_query_string = 'SELECT * FROM resume_book_internship'

    compounds = 0
    if companyName_query:
        sql_query_string += ' WHERE companyName_id = (SELECT companyName FROM resume_book_company AS c WHERE c.companyName=\"' + companyName_query + '\")'
        compounds += 1

    if numberRating_query:
        if compounds > 0: 
            sql_query_string += ' AND '
        else:
            sql_query_string += ' WHERE '
        sql_query_string += 'numberRating ' + equality_symbol + ' ' + numberRating_query

    queried_internships = Internship.objects.raw(sql_query_string)

    context = {
            'queried_internships': queried_internships,
            'netID_length': Internship._meta.get_field('netID').max_length,
            'companyName_length': Internship._meta.get_field('companyName').max_length,
            'numberRating_length': Internship._meta.get_field('numberRating'),
            'projectDescription_length': Internship._meta.get_field('projectDescription').max_length,
            'companyReview_length': Internship._meta.get_field('companyReview').max_length,
            'startDate': Internship._meta.get_field('startDate').max_length,
            'endDate': Internship._meta.get_field('endDate').max_length,
            'netid': request.user.username
            }
    
    if request.user.username == 'admin':
        return render(request, 'resume_book/internships.html', context)
    else:
        return render(request, 'resume_book/internships-noauth.html', context)

def addInternship(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    internshipNetID = request.POST.get('netID', 0)
    internshipCompanyName = request.POST.get('companyName')
    internshipNumberRating = request.POST.get('numberRating')
    internshipProjectDescription = request.POST.get('projectDescription')
    internshipCompanyReview = request.POST.get('companyReview')
    internshipStartDate = request.POST.get('startDate')
    internshipEndDate = request.POST.get('endDate')

    internshipProjectDescription.replace("'", "\\'")

    cursor = connection.cursor()
    q = 'SELECT * FROM resume_book_internship WHERE netID_id = \"{}\"'.format(internshipNetID)
    cursor.execute(q)
    rows = cursor.fetchall()

    q = 'SELECT * FROM resume_book_company WHERE companyName = \"{}\"'.format(internshipCompanyName)
    cursor.execute(q)
    rows_company = cursor.fetchall()

    if not rows_company:
        sql_query_string = """INSERT INTO resume_book_company (companyName, description, rating, sponsorDate) \n 
                                VALUES (\"{}\", \"{}\", {}, \"{}\");
                                """.format(internshipCompanyName, "", 0.0, datetime.datetime(1, 1, 1))
        cursor.execute(sql_query_string)

    if rows:
        existingInternship = rows[0]
        sql_query_string = 'UPDATE resume_book_internship \n SET '
        sql_query_string += 'numberRating = {}, '.format(internshipNumberRating if internshipNumberRating else existingInternship[1])
        sql_query_string += 'projectDescription = \"{}\", '.format(internshipProjectDescription if internshipProjectDescription else existingInternship[2])
        sql_query_string += 'companyReview = \'{}\', '.format(internshipCompanyReview if internshipCompanyReview else existingInternship[3])
        sql_query_string += 'startDate = \'{}\', '.format(internshipStartDate if internshipStartDate else existingInternship[4])
        sql_query_string += 'endDate = \'{}\', '.format(internshipEndDate if internshipEndDate else existingInternship[5])
        sql_query_string += 'companyName_id = \'{}\' \n'.format(internshipCompanyName if internshipCompanyName else existingInternship[0])
        sql_query_string += 'WHERE netID_id = \"{}\"; '.format(internshipNetID)
        cursor.execute(sql_query_string)

    else:
        if not internshipStartDate:
            internshipStartDate = datetime.datetime(1, 1, 1)

        if not internshipEndDate:
            internshipEndDate = datetime.datetime(1, 1, 1)

        if not internshipNumberRating:
            internshipNumberRating = 0
            
        if not internshipCompanyReview:
            internshipCompanyName = 0


        sql_query_string = """INSERT INTO resume_book_internship (numberRating, projectDescription, companyReview, startDate, endDate, companyName_id, netID_id) \n 
                                VALUES ({}, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\");
                                """.format(internshipNumberRating, internshipProjectDescription, internshipCompanyReview,
                                internshipStartDate, internshipEndDate, internshipCompanyName, internshipNetID)
        cursor.execute(sql_query_string)

    return HttpResponseRedirect(reverse('resume_book:internships'))

def removeInternship(request, internship_netID):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)
    netID = internship_netID.split()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_internship WHERE netID_id=\"{}\"'.format(netID[1]))

    return HttpResponseRedirect(reverse('resume_book:internships'))

def recruiters(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    name_query = request.GET.get('recruiterName', '')
    company_query = request.GET.get('companyName', '')
    sql_query_string = 'SELECT * FROM resume_book_recruiter'

    compounds = 0
    if name_query:
        sql_query_string += ' WHERE recruiterName=\"' + name_query + '\"'
        compounds += 1

    if company_query:
        if compounds == 0:
            sql_query_string += ' WHERE '
        else:
            sql_query_string += ' AND '
        sql_query_string += 'companyName_id=(SELECT companyName FROM resume_book_company AS c WHERE c.companyName=\"' + company_query + '\")'

    queried_recruiters = Recruiter.objects.raw(sql_query_string)

    context = {
            'queried_recruiters': queried_recruiters,
            'recruiter_name_length': Recruiter._meta.get_field('recruiterName').max_length,
            'company_name_length': Company._meta.get_field('companyName').max_length
            }
    
    if request.user.username == 'admin':
        return render(request, 'resume_book/recruiters.html', context)
    else:
        return render(request, 'resume_book/recruiters-noauth.html', context)

def addRecruiter(request):
    if not request.user.username == 'admin':
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    recruiterName = request.POST.get('recruiterName')
    recruiterCompanyName = request.POST.get('companyName')

    recruiterCompanyName.replace("'", "\\'")

    cursor = connection.cursor()
    q = 'SELECT * FROM resume_book_recruiter WHERE recruiterName = \"{}\"'.format(recruiterName)
    cursor.execute(q)
    rows = cursor.fetchall()

    q = 'SELECT * FROM resume_book_company WHERE companyName = \"{}\"'.format(recruiterCompanyName)
    cursor.execute(q)
    rows_company = cursor.fetchall()

    if not rows_company:
        sql_query_string = """INSERT INTO resume_book_company (companyName, description, rating, sponsorDate) \n 
                                VALUES (\"{}\", \"{}\", {}, \"{}\");
                                """.format(recruiterCompanyName, "", 0.0, datetime.datetime(1, 1, 1))
        cursor.execute(sql_query_string)

    if rows:
        existingRecruiter = rows[0]
        sql_query_string = 'UPDATE resume_book_recruiter \n SET '
        sql_query_string += 'companyName_id = \"{}\"'.format(recruiterCompanyName if recruiterCompanyName else existingRecruiter[1])
        sql_query_string += 'WHERE recruiterName = \"{}\";'.format(recruiterName)
        cursor.execute(sql_query_string)
    else:
        sql_query_string = """INSERT INTO resume_book_recruiter (recruiterName, companyName_id) \n 
                                VALUES (\'{}\', \'{}\');
                                """.format(recruiterName, recruiterCompanyName)
        cursor.execute(sql_query_string)

    return HttpResponseRedirect(reverse('resume_book:recruiters'))

def removeRecruiter(request, recruiter_name):
    if not request.user.username == 'admin':
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_recruiter WHERE recruiterName=\"{}\"'.format(recruiter_name))

    return HttpResponseRedirect(reverse('resume_book:recruiters'))

def students(request):
    if not request.user.is_authenticated:
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    name_query = request.GET.get('name', '')
    netID_query = request.GET.get('netID', '')

    equalitySymbol = request.GET.get('equality', '')
    gradYear_query = request.GET.get('gradYear', '')

    sql_query_string = 'SELECT * FROM resume_book_student'

    compounds = 0
    if name_query:
        sql_query_string += ' WHERE name = \"' + name_query + '\"'
        compounds += 1

    if netID_query:
        if compounds > 0: 
            sql_query_string += ' AND '
        else:
            sql_query_string += ' WHERE '
        sql_query_string += 'netid = \"' + netID_query + '\"'
        compounds += 1

    if gradYear_query:
        if compounds > 0: 
            sql_query_string += ' AND '
        else:
            sql_query_string += ' WHERE '
        sql_query_string += 'gradYear ' + equalitySymbol + ' ' + gradYear_query

    queried_students = Student.objects.raw(sql_query_string)

    context = {
            'queried_students': queried_students,
            'name_length': Student._meta.get_field('name').max_length,
            'netID_length': Student._meta.get_field('netID').max_length,
            'gradYear': Student._meta.get_field('gradYear'),
            'courseWork_length': Student._meta.get_field('courseWork').max_length,
            'projects_length': Student._meta.get_field('projects').max_length,
            'experiences': Student._meta.get_field('experiences').max_length,
            'netid':request.user.username
            }
    if request.user.username == 'admin':
        return render(request, 'resume_book/students.html', context)
    if resumeAuth.userInGroup(request.user, 'Student'):
        return render(request, 'resume_book/students-student.html', context)
    else:
        return render(request, 'resume_book/students-recruiter.html', context)

def addStudent(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    # insert into sql
    studentNetID = request.POST.get('netID', request.user.username) # If no netID provided, use the current user's
    studentName = request.POST.get('name', request.user.username) # Also pretend netID is name if none is provided
    studentGradYear = request.POST.get('gradYear', 0)
    studentCourseWork = request.POST.get('courseWork', '')
    studentProjects = request.POST.get('projects', '')
    studentExperiences = request.POST.get('experiences', '')

    studentCourseWork.replace("'", "\\'")
    studentProjects.replace("'", "\\'")
    studentExperiences.replace("'", "\\'")

    # insert into neo4j
    interests = request.POST.get('interests', '').split(',')
    skills = request.POST.get('skills', '').split(',')

    cursor = connection.cursor()
    q = 'SELECT * FROM resume_book_student WHERE netID = \"{}\"'.format(studentNetID)
    cursor.execute(q)
    rows = cursor.fetchall()
    if rows:
        existingStudent = rows[0]
        sql_query_string = 'UPDATE resume_book_student \n SET '
        sql_query_string += 'name = \"{}\", '.format(studentName if studentName else existingStudent[1])
        sql_query_string += 'gradYear = {}, '.format(studentGradYear if studentGradYear else existingStudent[4])
        sql_query_string += 'courseWork = \"{}\", '.format(studentCourseWork if studentCourseWork else existingStudent[2])
        sql_query_string += 'projects = \"{}\", '.format(studentProjects if studentProjects else existingStudent[5])
        sql_query_string += 'experiences = \"{}\" \n'.format(studentExperiences if studentExperiences else existingStudent[3])
        sql_query_string += 'WHERE netID = \"{}\"; '.format(studentNetID)
        cursor.execute(sql_query_string)

    else:
        sql_query_string = """INSERT INTO resume_book_student (name, netID, gradYear, courseWork, projects, experiences) \n 
                                VALUES (\'{}\', \'{}\', {}, \'{}\', \'{}\', \'{}\');
                                """.format(studentName, studentNetID, studentGradYear, studentCourseWork, studentProjects, studentExperiences)
        cursor.execute(sql_query_string)

    session = driver.session()

    relation = session.run('MATCH (s:Student) WHERE s.netid={netid} RETURN s', netid=studentNetID)
    count = 0
    for node in relation:
        count += 1
    if count == 0:
        session.run('CREATE (s:Student {netid:{netid}})', netid=studentNetID)

    for interest in interests:
        if interest == '':
            continue
        interest = interest.lower().strip()
        interest_node = session.run('MATCH (k:Interest) WHERE k.value={interest_name} RETURN k', interest_name=interest)

        count = 0
        for node in interest_node:
            count += 1
        if count == 0:
            session.run('CREATE (k:Interest {value:{interest_name}})', interest_name=interest)
            
            
        count = 0 
        relation = session.run('MATCH (s:Student)-[a:InterestedIn]->(k:Interest) WHERE s.netid={netid} AND k.value={interest_name} RETURN a', netid=studentNetID, interest_name=interest)
        for node in relation:
            count += 1

        if count == 0:
            session.run('MATCH (s:Student), (k:Interest) WHERE s.netid={netid} AND k.value={interest_name} CREATE (s)-[:InterestedIn]->(k)', netid=studentNetID, interest_name=interest)

    for skill in skills:
        if skill == '':
            continue
        skill = skill.lower().strip()
        skill_node = session.run('MATCH (k:Skill) WHERE k.value={skill_name} RETURN k', skill_name=skill)

        count = 0
        for node in skill_node:
            count += 1
        if count == 0:
            session.run('CREATE (k:Skill {value:{skill_name}})', skill_name=skill)

        count = 0 
        relation = session.run('MATCH (s:Student)-[a:SkilledIn]->(k:Skill) WHERE s.netid={netid} AND k.value={skill_name} RETURN a', netid=studentNetID, skill_name=skill)
        for node in relation:
            count += 1

        if count == 0:
            session.run('MATCH (s:Student), (k:Skill) WHERE s.netid={netid} AND k.value={skill_name} CREATE (s)-[:SkilledIn]->(k)', netid=studentNetID, skill_name=skill)

    session.close()

    return HttpResponseRedirect(reverse('resume_book:students'))

def removeStudent(request, student_netID):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_student WHERE netID=\"{}\"'.format(student_netID))

    session = driver.session()
    session.run('MATCH (s:Student) WHERE s.netid={netid} DETACH DELETE s', netid=student_netID)
    session.close()

    return HttpResponseRedirect(reverse('resume_book:students'))

def interestSearch(request):
    if not request.user.is_authenticated:
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)
        
    interest_string = request.GET.get('interests', '').split(',')
    conjunction = request.GET.get('conjunction')
    
    session = driver.session()

    neo4j_result = []
    if conjunction == 'OR':
        neo4j_query_string = 'MATCH (a:Student)'

        compounds=0
        for word in interest_string:
            if not word: pass

            word = word.strip()
            
            if compounds == 0:
                neo4j_query_string += '-[i:InterestedIn]->(v:Interest) WHERE '
            else:
                neo4j_query_string += ' ' + conjunction + ' '

            compounds += 1

            neo4j_query_string += 'v.value=\"' + word + '\"'

        neo4j_query_string += ' RETURN a.netid'
        neo4j_result = session.run(neo4j_query_string)
        
    elif conjunction == 'AND':
        neo4j_result = session.run('MATCH (a:Student)-[i:InterestedIn]->(v:Interest) WHERE v.value=\"' + interest_string[0] + '\" RETURN a.netid')
        neo4j_result = set(neo4j_result)

        for word in interest_string[1:]:
            if not word: pass

            word = word.strip()

            result = session.run('MATCH (a:Student)-[i:InterestedIn]->(v:Interest) WHERE v.value=\"' + word + '\" RETURN a.netid')

            neo4j_result = neo4j_result.intersection(set(result))

    netid_list = []
    for record in neo4j_result:
        netid_list.append(record['a.netid'])
    session.close()

    sql_query_string = 'SELECT * FROM resume_book_student'

    if len(netid_list) > 0:
        sql_query_string += ' WHERE netid IN %s'
    else:
        return render(request, 'resume_book/interestSearch.html')

    sql_result = Student.objects.raw(sql_query_string, params=[netid_list])

    context = {
        'queried_students': sql_result,
        'name_length': Student._meta.get_field('name').max_length,
        'netID_length': Student._meta.get_field('netID').max_length,
        'gradYear': Student._meta.get_field('gradYear'),
        'courseWork_length': Student._meta.get_field('courseWork').max_length,
        'projects_length': Student._meta.get_field('projects').max_length,
        'experiences': Student._meta.get_field('experiences').max_length
    }

    return render(request, 'resume_book/interestSearch.html', context)

def skillSearch(request):
    if not request.user.is_authenticated:
        return HttpResponse(NOT_AUTHENTICATED_RESPONSE)

    skill_string = request.GET.get('skills', '').split(',')
    conjunction = request.GET.get('conjunction')
    
    session = driver.session()

    neo4j_result = []
    if conjunction == 'OR':
        neo4j_query_string = 'MATCH (a:Student)'

        compounds=0
        for word in skill_string:
            if not word: pass

            word = word.strip()
            
            if compounds == 0:
                neo4j_query_string += '-[i:SkilledIn]->(v:Skill) WHERE '
            else:
                neo4j_query_string += ' ' + conjunction + ' '

            compounds += 1

            neo4j_query_string += 'v.value=\"' + word + '\"'

        neo4j_query_string += ' RETURN a.netid'
        neo4j_result = session.run(neo4j_query_string)
        
    elif conjunction == 'AND':
        neo4j_result = session.run('MATCH (a:Student)-[i:SkilledIn]->(v:Skill) WHERE v.value=\"' + skill_string[0] + '\" RETURN a.netid')
        neo4j_result = set(neo4j_result)

        for word in skill_string[1:]:
            if not word: pass

            word = word.strip()

            result = session.run('MATCH (a:Student)-[i:SkilledIn]->(v:Skill) WHERE v.value=\"' + word + '\" RETURN a.netid')

            neo4j_result = neo4j_result.intersection(set(result))

    netid_list = []
    for record in neo4j_result:
        netid_list.append(record['a.netid'])
    session.close()

    sql_query_string = 'SELECT * FROM resume_book_student'

    if len(netid_list) > 0:
        sql_query_string += ' WHERE netid IN %s'
    else:
        return render(request, 'resume_book/skillSearch.html')

    sql_result = Student.objects.raw(sql_query_string, params=[netid_list])

    context = {
        'queried_students': sql_result,
        'name_length': Student._meta.get_field('name').max_length,
        'netID_length': Student._meta.get_field('netID').max_length,
        'gradYear': Student._meta.get_field('gradYear'),
        'courseWork_length': Student._meta.get_field('courseWork').max_length,
        'projects_length': Student._meta.get_field('projects').max_length,
        'experiences': Student._meta.get_field('experiences').max_length
    }

    return render(request, 'resume_book/skillSearch.html', context)
