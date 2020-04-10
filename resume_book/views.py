from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Q


from .models import StudentGroup;
from .models import Company;
from .models import Internship;
from .models import Recruiter;
from .models import Student;

# Create your views here.
def index(request):
    return HttpResponse('Hello, world. You\'re at the reusmebook index.')


def studentGroups(request):
    all_student_groups = StudentGroup.objects.all()

    context = {
            'all_student_groups': all_student_groups,
            'name_length': StudentGroup._meta.get_field('name').max_length,
            'desc_length': StudentGroup._meta.get_field('description').max_length
            }
    return render(request, 'resume_book/studentGroups.html', context)

def addGroup(request):
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

def removeGroup(request, group_name):
    group = get_object_or_404(StudentGroup, pk=group_name)
    group.delete()

    return HttpResponseRedirect(reverse('resume_book:studentGroups'))

def companies(request):
    name_query = request.GET.get('companyName', '')
    rating_query = request.GET.get('rating', '')


    combined_query = Q(name__icontains=name_query)
    # the 'icontains' is case-insensitive, while 'contains' is sensitive

    if rating_query != '':
        rating = int(rating_query)
        if equalitySymbol == '>':
            combined_query = Q(rating__gt=rating)
        elif equalitySymbol == '<':
            combined_query = Q(rating__lt=rating)
        else:
            combined_query = Q(rating=rating)


    queried_companies = Company.objects.filter(combined_query)
        

    context = {
            'queried_companies': queried_companies,
            'name_length': Company._meta.get_field('companyName').max_length,
            'desc_length': Company._meta.get_field('description').max_length,
            'rating': Company._meta.get_field('rating'),
            'sponsorDate': Company._meta.get_field('sponsorDate').max_length,

            }
    return render(request, 'resume_book/companies.html', context)

def addCompany(request):
    companyName = request.POST.get('companyName')
    companyDescription = request.POST.get('description', False)
    companyRating = request.POST.get('rating', False)
    companySponsorDate = request.POST.get('sponsorDate')

    try:
        # If exists, update it!
        existingCompany = Company.objects.get(pk=companyName)
        existingCompany.description = companyDescription
        existingCompany.rating = companyRating
        existingCompany.sponsorDate = companySponsorDate
        existingCompany.save()

    except Company.DoesNotExist:
        # If doesn't exists, create one!
        newCompany = Company(companyName=companyName, description=companyDescription, rating=companyRating, sponsorDate=companySponsorDate)
        newCompany.save()

    return HttpResponseRedirect(reverse('resume_book:companies'))

def removeCompany(request, company_name):
    company = get_object_or_404(Company, pk=company_name)
    company.delete()

    return HttpResponseRedirect(reverse('resume_book:companies'))


def internships(request):
    all_internships = Internship.objects.all()[:5]

    context = {
            'all_internships': all_internships,
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
    internship = get_object_or_404(Internship, pk=internship_netID)
    internship.delete()

    return HttpResponseRedirect(reverse('resume_book:internships'))

def recruiters(request):
    all_recruiters = Recruiter.objects.all()[:5]

    context = {
            'all_recruiters': all_recruiters,
            'recruiter_name_length': Recruiter._meta.get_field('recruiterName').max_length,
            'company_name_length': Company._meta.get_field('companyName').max_length
            }
    return render(request, 'resume_book/recruiters.html', context)

def addRecruiter(request):
    recruiterName = request.POST.get('recruiterName')
    recruiterCompanyName = request.POST.get('companyName')

    try:
        # If exists, update it!
        existingRecruiter = Recruiter.objects.get(pk=recruiterName)
        existingRecruiter.companyName = Company.objects.get(companyName=recruiterCompanyName)
        existingRecruiter.save()

    except Recruiter.DoesNotExist:
        # If doesn't exists, create one!
        newRecruiter = Recruiter(recruiterName=recruiterName, companyName=Company.objects.get(companyName=recruiterCompanyName))
        newRecruiter.save()

    return HttpResponseRedirect(reverse('resume_book:recruiters'))

def removeRecruiter(request, recruiter_name):
    recruiter = get_object_or_404(Recruiter, pk=recruiter_name)
    recruiter.delete()

    return HttpResponseRedirect(reverse('resume_book:recruiters'))

def students(request):
    name_query = request.GET.get('name', '')
    netID_query = request.GET.get('netID', '')

    equalitySymbol = request.GET.get('equality', '')
    gradYear_query = request.GET.get('gradYear', '')


    combined_query = Q(name__icontains=name_query, netID__icontains=netID_query)
    # the 'icontains' is case-insensitive, while 'contains' is sensitive

    if gradYear_query != '':
        gradYear = int(gradYear_query)
        if equalitySymbol == '>':
            combined_query = Q(gradYear__gt=gradYear)
        elif equalitySymbol == '<':
            combined_query = Q(gradYear__lt=gradYear)
        else:
            combined_query = Q(gradYear=gradYear)


    queried_students = Student.objects.filter(combined_query)
        

    context = {
            'queried_students': queried_students,
            'name_length': Student._meta.get_field('name').max_length,
            'netID_length': Student._meta.get_field('netID').max_length,
            'interests_length': Student._meta.get_field('interests').max_length,
            'gradYear': Student._meta.get_field('gradYear'),
            'courseWork_length': Student._meta.get_field('courseWork').max_length,
            'projects_length': Student._meta.get_field('projects').max_length,
            'experiences': Student._meta.get_field('experiences').max_length
            }
    return render(request, 'resume_book/students.html', context)

def addStudent(request):
    studentName = request.POST.get('name')
    studentNetID = request.POST.get('netID')
    studentInterests = request.POST.get('interests', False)
    studentGradYear = request.POST.get('gradYear', 0) if request.POST.get('gradYear') else int(0)
    studentCourseWork = request.POST.get('courseWork')
    studentProjects = request.POST.get('projects', False)
    studentExperiences = request.POST.get('experiences', False)

    try:
        # If exists, update it!
        existingStudent = Student.objects.get(pk=studentNetID)
        existingStudent.name = studentName if studentName else existingStudent.name
        existingStudent.netID = studentNetID if studentNetID else existingStudent.netID
        existingStudent.interests = studentInterests if studentInterests else existingStudent.interests
        existingStudent.gradYear = int(studentGradYear) if studentGradYear else existingStudent.gradYear
        existingStudent.courseWork = studentCourseWork if studentCourseWork else existingStudent.courseWork
        existingStudent.projects = studentProjects if studentProjects else existingStudent.projects
        existingStudent.experiences = studentExperiences if studentExperiences else existingStudent.experiences
        existingStudent.save()

    except Student.DoesNotExist:
        # If doesn't exists, create one!
        newStudent = Student(netID=studentNetID, name=studentName, 
                    interests=studentInterests, gradYear=studentGradYear,
                    courseWork=studentCourseWork, projects=studentProjects,
                    experiences=studentExperiences
                    )
        newStudent.save()

    return HttpResponseRedirect(reverse('resume_book:students'))

def removeStudent(request, student_netID):
    student = get_object_or_404(Student, pk=student_netID)
    student.delete()

    return HttpResponseRedirect(reverse('resume_book:students'))

