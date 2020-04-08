from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .models import StudentGroup;
from .models import Company;
from .models import Internship;
from .models import Recruiter;
from .models import Student;

# Create your views here.
def index(request):
    return HttpResponse('Hello, world. You\'re at the reusmebook index.')


def studentGroups(request):
    all_student_groups = StudentGroup.objects.all()[:5]

    context = {
            'all_student_groups': all_student_groups,
            'name_length': StudentGroup._meta.get_field('name').max_length,
            'desc_length': StudentGroup._meta.get_field('description').max_length
            }
    return render(request, 'resume_book/studentGroups.html', context)

def addGroup(request):
    groupName = request.POST['name']
    groupDescription = request.POST['description']

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
    all_companies = Company.objects.all()[:5]

    context = {
            'all_companies': all_companies,
            'name_length': Company._meta.get_field('companyName').max_length,
            'desc_length': Company._meta.get_field('description').max_length,
            'rating': Company._meta.get_field('rating'),
            'sponsorDate': Company._meta.get_field('sponsorDate').max_length,

            }
    return render(request, 'resume_book/companies.html', context)

def addCompany(request):
    companyName = request.POST['companyName']
    companyDescription = request.POST['description']
    companyRating = request.POST['rating']
    companySponsorDate = request.POST['sponsorDate']

    try:
        # If exists, update it!
        existingCompany = Company.objects.get(pk=companyName)
        existingCompany.description = companyDescription
        existingCompany.rating = companyRating
        existingCompany.sponsorDate = companySponsorDate
        existingCompany.save()

    except Company.DoesNotExist:
        # If doesn't exists, create one!
        newCompany = Company(name=companyName, description=companyDescription, rating=companyRating, sponsorDate=companySponsorDate)
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
    internshipNetID = request.POST['netID']
    internshipCompanyName = request.POST['companyName']
    internshipNumberRating = request.POST['numberRating']
    internshipProjectDescription = request.POST['projectDescription']
    internshipCompanyReview = request.POST['companyReview']
    internshipExperiences = request.POST['experiences']
    internshipStartDate = request.POST['startDate']
    internshipEndDate = request.POST['endDate']

    try:
        # If exists, update it!
        existingInternship = Internship.objects.get(pk=internshipID)
        existingInternship.netID = internshipNetID
        existingInternship.companyName = internshipCompanyName
        existingInternship.numberRating = internshipNumberRating
        existingInternship.projectDescription = internshipProjectDescription
        existingInternship.companyReview = internshipCompanyReview
        existingInternship.experiences = internshipExperiences
        existingInternship.startDate = internshipStartDate
        existingInternship.endDate = internshipEndDate
        existingInternship.save()

    except Internship.DoesNotExist:
        # If doesn't exists, create one!
        newInternship = Internship(netID=internshipNetID, companyName=internshipCompanyName, 
                        numberRating=internshipNumberRating, projectDescription= internshipProjectDescription, 
                        companyReview=internshipCompanyReview, experiences=internshipExperiences,
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
            'company_name_length': Recruiter._meta.get_field('companyName').max_length
            }
    return render(request, 'resume_book/recruiters.html', context)

def addRecruiter(request):
    recruiterName = request.POST['name']
    recruiterCompanyName = request.POST['companyName']

    try:
        # If exists, update it!
        existingRecruiter = Recruiter.objects.get(pk=recruiterName)
        existingRecruiter.companyName = recruiterCompanyName
        existingRecruiter.save()

    except Recruiter.DoesNotExist:
        # If doesn't exists, create one!
        newRecruiter = Recruiter(recruiterName=recruiterName, companyName=recruiterCompanyName)
        newRecruiter.save()

    return HttpResponseRedirect(reverse('resume_book:Recruiter'))

def removeRecruiter(request, recruiter_name):
    recruiter = get_object_or_404(Recruiter, pk=recruiter_name)
    recruiter.delete()

    return HttpResponseRedirect(reverse('resume_book:Recruiter'))

def students(request):
    all_students = Student.objects.all()[:5]

    context = {
            'all_students': all_students,
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
    studentName = request.POST['name']
    studentNetID = request.POST['netID']
    studentInterests = request.POST.get('interests', False)
    studentGradYear = request.POST['gradYear']
    studentCourseWork = request.POST.get('courseWork', 'fjsdkljs')
    studentProjects = request.POST.get('projects', False)
    studentExperiences = request.POST.get('experiences', False)

    try:
        # If exists, update it!
        existingStudent = Student.objects.get(pk=studentNetID)
        existingStudent.name = studentName
        existingStudent.netID = studentNetID
        existingStudent.interests = studentInterests
        existingStudent.gradYear = studentGradYear 
        existingStudent.courseWork = studentCourseWork
        existingStudent.projects = studentProjects 
        existingStudent.save()

    except Student.DoesNotExist:
        # If doesn't exists, create one!
        newStudent = Student(netID=studentNetID, name=studentName, 
                    interests=studentInterests, gradYear=studentGradYear,
                    courseWork=studentCourseWork, projects=studentProjects
                    )
        newStudent.save()

    return HttpResponseRedirect(reverse('resume_book:Student'))

def removeStudent(request, student_name):
    student = get_object_or_404(Student, pk=student_name)
    student.delete()

    return HttpResponseRedirect(reverse('resume_book:Student'))
