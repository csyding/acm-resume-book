from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .models import StudentGroup;
from .models import Company;
from .models import Resume;

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
            'sponsorDate': Company._meta.get_field('sponsorDate'),

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


def resumes(request):
    all_resumes = Resume.objects.all()[:5]

    context = {
            'all_resumes': all_resumes,
            'netID': Resume._meta.get_field('netID').max_length,
            'resumeID': Resume._meta.get_field('resumeID'),
            'gradYear': Company._meta.get_field('gradYear'),
            'courseWork_length': Resume._meta.get_field('courseWork').max_length,
            'projects_length': Resume._meta.get_field('projects').max_length,
            'experiences_length': Resume._meta.get_field('experiences').max_length,
            }
    return render(request, 'resume_book/resumes.html', context)

def addResume(request):
    resumeNetID = request.POST['netID']
    resumeResumeID = request.POST['resumeID']
    resumeGradYear = request.POST['gradYear']
    resumeCourseWork = request.POST['courseWork']
    resumeProjects = request.POST['projects']
    resumeExperiences = request.POST['experiences']

    try:
        # If exists, update it!
        existingResume = Resume.objects.get(pk=resumeID)
        existingResume.netID = resumeNetID
        existingResume.gradYear = resumeGradYear
        existingResume.courseWork = resumeCourseWork
        existingResume.projects = resumeProjects
        existingResume.experiences = resumeExperiences
        existingResume.save()

    except Resume.DoesNotExist:
        # If doesn't exists, create one!
        newResume = Resume(netID=resumeNetID, gradYear=rresumeGradYear, courseWork=resumeCourseWork, projects = resumeProjects, experiences = resumeExperiences)
        newResume.save()

    return HttpResponseRedirect(reverse('resume_book:resumes'))

def removeResume(request, resume_name):
    resume = get_object_or_404(Resume, pk=resume_name)
    resume.delete()

    return HttpResponseRedirect(reverse('resume_book:resumes'))

