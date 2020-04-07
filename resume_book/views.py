from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .models import StudentGroup;

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
            'name_length': Company._meta.get_field('name').max_length,
            'desc_length': Company._meta.get_field('description').max_length
            }
    return render(request, 'resume_book/companies.html', context)

def addCompany(request):
    companyName = request.POST['name']
    companyDescription = request.POST['description']
    companyRating = request.POST['rating']
    companySponsorDate = request.POST['sponsorDate']

    try:
        # If exists, update it!
        existingCompany = Company.objects.get(pk=groupName)
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

