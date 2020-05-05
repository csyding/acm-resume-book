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

from datetime import date
from datetime import datetime

graphenedb_url = os.environ.get("GRAPHENEDB_BOLT_URL")
graphenedb_user = os.environ.get("GRAPHENEDB_BOLT_USER")
graphenedb_pass = os.environ.get("GRAPHENEDB_BOLT_PASSWORD")

driver = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))

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

def studentHome(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse('You\'re not allowed to view this page!')

    return render(request, 'resume_book/studentHome.html')

def recruiterHome(request):
    if not resumeAuth.userInGroup(request.user, 'Recruiter'):
        return HttpResponse('You\'re not allowed to view this page!')

    return render(request, 'resume_book/recruiterHome.html')

def studentGroups(request):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    name_query = request.GET.get('name', '')

    sql_query_string = 'SELECT * FROM resume_book_studentgroups'

    if name_query:
        sql_query_string += ' WHERE name=' + name_query

    StudentGroup.objects.raw(sql_query_string)

    context = {
            'queried_studentGroups': queried_studentGroups,
            'name_length': StudentGroup._meta.get_field('name').max_length,
            'desc_length': StudentGroup._meta.get_field('description').max_length
            }
    return render(request, 'resume_book/studentGroups.html', context)

def addGroup(request):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    groupName = request.POST.get('name')
    groupDescription = request.POST.get('description')

    try:
        # If exists, update it!
        existingGroup = StudentGroup.objects.get(pk=groupName)
        existingGroup.description = groupDescription
        existingGroup.save()

    except StudentGroup.DoesNotExist:
        # If doesn't exists, create one!
        newGroup = StudentGroup(name=groupName, description=groupDescription)
        newGroup.save()

    return HttpResponseRedirect(reverse('resume_book:studentGroups'))

def addStudentToGroup(request):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    groupName = request.POST.get('name')
    netID = request.POST.get('netID')

    try:
        existingGroup = StudentGroup.objects.get(pk=groupName)
        existingStudent = Student.objects.get(pk=netID)
        existingGroup.members.add(existingStudent)
        print(existingGroup.members.all)

    except StudentGroup.DoesNotExist:
        print ('Student Group does not exist!')

    return HttpResponseRedirect(reverse('resume_book:studentGroups'))


def removeGroup(request, group_name):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    StudentGroup.objects.raw('DELETE FROM resume_book_studentgroup WHERE name=\"%s\"', params=[group_name])

    return HttpResponseRedirect(reverse('resume_book:studentGroups'))

def companies(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse('You\'re not allowed to view this page!')

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
    return render(request, 'resume_book/companies.html', context)

def addCompany(request):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    companyName = request.POST.get('companyName')
    companyDescription = request.POST.get('description', False)
    companyRating = request.POST.get('rating', False)
    companySponsorDate = request.POST.get('sponsorDate')

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
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_company WHERE companyName=\"{}\"'.format(company_name))
    return HttpResponseRedirect(reverse('resume_book:companies'))


def internships(request):
    if not resumeAuth.userInGroup(request.user, 'Student'):
        return HttpResponse('You\'re not allowed to view this page!')

    companyName_query = request.GET.get('companyName', '')
    equality_symbol = request.GET.get('equality', '')
    numberRating_query = request.GET.get('numberRating', '')

    sql_query_string = 'SELECT * FROM resume_book_internship'

    compounds = 0
    if companyName_query:
        sql_query_string += ' WHERE companyName = \"' + companyName_query + '\"'
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
            }
    return render(request, 'resume_book/internships.html', context)

def addInternship(request):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    internshipNetID = request.POST.get('netID', 0)
    internshipCompanyName = request.POST.get('companyName')
    internshipNumberRating = request.POST.get('numberRating')
    internshipProjectDescription = request.POST.get('projectDescription')
    internshipCompanyReview = request.POST.get('companyReview')
    internshipStartDate = request.POST.get('startDate')
    internshipEndDate = request.POST.get('endDate')

    try:
        # If exists, update it!
        existingInternship = Internship.objects.get(pk=internshipNetID)
        existingInternship.netID = Student.objects.get(netID=internshipNetID)
        existingInternship.companyName = Company.objects.get(companyName=internshipCompanyName)
        existingInternship.numberRating = internshipNumberRating if internshipNumberRating else existingInternship.numberRating
        existingInternship.projectDescription = internshipProjectDescription if internshipProjectDescription else existingInternship.projectDescription
        existingInternship.companyReview = internshipCompanyReview if internshipCompanyReview else existingInternship.companyReview
        existingInternship.startDate = internshipStartDate if internshipStartDate else existingInternship.startDate
        existingInternship.endDate = internshipEndDate if internshipEndDate else existingInternship.endDate
        existingInternship.save()

    except Internship.DoesNotExist:
        # If doesn't exists, create one!
        newInternship = Internship(netID=Student.objects.get(netID=internshipNetID), 
                        companyName=Company.objects.get(companyName=internshipCompanyName), 
                        numberRating=internshipNumberRating, projectDescription= internshipProjectDescription, 
                        companyReview=internshipCompanyReview,
                        startDate=internshipStartDate, endDate=internshipEndDate)
        newInternship.save()

    return HttpResponseRedirect(reverse('resume_book:internships'))

def removeInternship(request, internship_netID):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    Internship.objects.raw('DELETE FROM resume_book_internship WHERE netID=\"%s\"', params=[internship_netID])

    return HttpResponseRedirect(reverse('resume_book:internships'))

def recruiters(request):
    if not resumeAuth.userInGroup(request.user, 'Recruiter'):
        return HttpResponse('You\'re not allowed to view this page!')

    name_query = request.GET.get('recruiterName', '')

    sql_query_string = 'SELECT * FROM resume_book_recruiter'

    if name_query:
        sql_query_string += ' WHERE recruiterName=\"' + name_query + '\"'

    queried_recruiters = Recruiter.objects.raw(sql_query_string)

    context = {
            'queried_recruiters': queried_recruiters,
            'recruiter_name_length': Recruiter._meta.get_field('recruiterName').max_length,
            'company_name_length': Company._meta.get_field('companyName').max_length
            }
    return render(request, 'resume_book/recruiters.html', context)

def addRecruiter(request):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    recruiterName = request.POST.get('recruiterName')
    recruiterCompanyName = request.POST.get('companyName')

    cursor = connection.cursor()
    q = 'SELECT * FROM resume_book_recruiter WHERE recruiterName = \"{}\"'.format(recruiterName)
    cursor.execute(q)
    rows = cursor.fetchall()
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
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_recruiter WHERE recruiterName=\"{}\"'.format(recruiter_name))

    return HttpResponseRedirect(reverse('resume_book:recruiters'))

def students(request):
    if not resumeAuth.userInGroup(request.user, 'Recruiter'):
        return HttpResponse('You\'re not allowed to view this page!')

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
            'experiences': Student._meta.get_field('experiences').max_length
            }
    return render(request, 'resume_book/students.html', context)

def addStudent(request):
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    # insert into sql
    studentName = request.POST.get('name')
    studentNetID = request.POST.get('netID')
    studentGradYear = request.POST.get('gradYear', 0) if request.POST.get('gradYear') else int(0)
    studentCourseWork = request.POST.get('courseWork')
    studentProjects = request.POST.get('projects', False)
    studentExperiences = request.POST.get('experiences', False)

    # insert into neo4j
    interests = request.POST.get('interests').split(',')
    skills = request.POST.get('skills').split(',')

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
    if not request.user.is_authenticated:
        return HttpResponse('You\'re not allowed to view this page!')

    cursor = connection.cursor()
    cursor.execute('DELETE FROM resume_book_student WHERE netid=\"\"'.format(student_netID))
    session = driver.session()
    session.run('MATCH (s:Student) WHERE s.netid={netid} DETACH DELETE s', netid=student_netID)
    session.close()

    return HttpResponseRedirect(reverse('resume_book:students'))

def interestSearch(request):
    interest_string = request.GET.get('interests', '')

    if (interest_string):
        session = driver.session()
        neo4j_result = session.run('MATCH (a:Student)-[i:InterestedIn]->(v:Interest) WHERE v.value={interest} RETURN a.netid', interest=interest_string)
        
        netid_list = []
        for record in neo4j_result:
            netid_list.append(record["a.netid"])
        session.close()

        if len(netid_list) == 0:
            return render(request, 'resume_book/interestSearch.html')

        sql_result = Student.objects.raw('SELECT * FROM resume_book_student WHERE netid IN %s', params=[tuple(netid_list)])

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

    return render(request, 'resume_book/interestSearch.html')

def skillSearch(request):
    skill_string = request.GET.get('skills', '')

    if (skill_string):
        session = driver.session()
        neo4j_result = session.run('MATCH (a:Student)-[i:SkilledIn]->(v:Skill) WHERE v.value={skill} RETURN a.netid', skill=skill_string)
        
        netid_list = []
        for record in neo4j_result:
            netid_list.append(record["a.netid"])
        session.close()

        if len(netid_list) == 0:
            return render(request, 'resume_book/skillSearch.html')

        sql_result = Student.objects.raw('SELECT * FROM resume_book_student WHERE netid IN %s', params=[tuple(netid_list)])

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

    return render(request, 'resume_book/skillSearch.html')    
