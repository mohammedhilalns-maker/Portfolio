from django.contrib.auth import authenticate,login
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

def admin_home(request):
    return render(request,'admin_home.html')

def admin_view_about(request):
    abouts = About.objects.all()
    return render(request, 'admin_view_about.html', {'abouts':abouts})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('a')
        password = request.POST.get('b')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_home')
            pass

        return render(request, 'login.html', {'error': 'Wrong username or password'})

    return render(request, 'login.html')





def about(request):
    return render(request,'about.html')


def add_about(request):
    if request.method=='POST':
       form = AboutForm(request.POST,request.FILES)
       if form.is_valid():
          form.save()
          return redirect('resume')
    else:
        form = AboutForm()
    return render(request, 'add_about.html', {'form':form})

def update_about(request, id):
    abouts = get_object_or_404(About, id=id)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=abouts)
        if form.is_valid():
            form.save()
            return redirect('admin_view_about')
    else:
        form = AboutForm(instance=abouts)
    return render(request, 'update_about.html', {'form':form})

def resume(request):
    abouts = About.objects.all()
    person = Addpersonaldetail.objects.all()
    edu = Education.objects.all().order_by('-id')
    experience = WorkExperience.objects.all().order_by('-id')
    certify = Crtification.objects.all().order_by('-id')
    lan = Language.objects.all().order_by('-id')
    skil = SKILL.objects.all().order_by('-id')
    return render(request, 'resume.html', {
        'abouts': abouts,
        'person': person,
        'edu':edu,
        'experience': experience,
        'certify': certify,
        'lan': lan,
        'skil': skil,
    })

def add_personal_details(request):
    if request.method=='POST':
        form = PersonaldetailsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = PersonaldetailsForm()
    return render(request, 'add_personal_details.html', {'form':form})

def add_education(request):
    if request.method=='POST':
        form = EducationalDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = EducationalDetailsForm()
    return render(request, 'add_education.html', {'form':form})


def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            if experience.Status == 'working':
                experience.Duration = None
                experience.StartDate = None
                experience.EndDate = None

            experience.save()
            return redirect('resume')
    else:
        form = ExperienceForm()
    return render(request, 'add_experience.html', {'form': form})

def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = CertificateForm()
    return render(request, 'add_certificate.html', {'form':form})

def add_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = LanguageForm()
    return render(request, 'add_language.html', {'form':form})

def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = SkillForm()
    return render(request, 'add_skill.html', {'form':form})

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def view_contact(request):
    cnt = Contact.objects.all()
    return render(request,'view_contact.html', {'cnt':cnt})