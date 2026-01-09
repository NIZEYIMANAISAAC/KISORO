from django.shortcuts import render, redirect, get_object_or_404
from .models import SiteInfo, QuickLink, Event, News, Testimonial, Achievement, StaffMember, Facility, AboutPage, Department, Program, Subject, AcademicCalendarEntry, AcademicResult, AdmissionApplication, Club, Activity, SportTeam, StudentCouncilMember, DisciplinePolicy, CounselingResource, TransportRoute, ParentNotice
from .forms import AdmissionForm


def staff_list(request):
    staff = StaffMember.objects.filter(public_profile=True)
    context = {'staff': staff}
    return render(request, 'vision/staff_list.html', context)


def staff_detail(request, pk):
    staff = get_object_or_404(StaffMember, pk=pk, public_profile=True)
    context = {'staff': staff}
    return render(request, 'vision/staff_detail.html', context)


def home(request):
    siteinfo, created = SiteInfo.objects.get_or_create(
        defaults={
            'school_name': 'Kisoro Vision Secondary School',
            'motto': 'Knowledge, Integrity, Service',
            'principal_name': 'The Principal',
            'principal_message': 'Welcome to Kisoro Vision Secondary School. We are committed to excellence.',
            'contact_email': 'info@kisorovision.ac.ug',
            'contact_phone': '+256 000 000 000',
            'address': 'P.O. Box, Kisoro, Uganda',
            'admissions_open': True
        }
    )
    quick_links = QuickLink.objects.all()[:6]
    events = Event.objects.all().order_by('date')[:5]
    news = News.objects.all()[:5]
    testimonials = Testimonial.objects.all()[:3]
    achievements = Achievement.objects.all()[:4]
    context = {
        'siteinfo': siteinfo,
        'quick_links': quick_links,
        'events': events,
        'news': news,
        'testimonials': testimonials,
        'achievements': achievements,
    }
    return render(request, 'vision/home.html', context)


def about(request):
    about = AboutPage.objects.first()
    staff = StaffMember.objects.filter(is_leadership=False)
    leadership = StaffMember.objects.filter(is_leadership=True)
    facilities = Facility.objects.all()
    context = {
        'about': about,
        'staff': staff,
        'leadership': leadership,
        'facilities': facilities,
    }
    return render(request, 'vision/about.html', context)


def academics(request):
    departments = Department.objects.all()
    programs = Program.objects.all()
    subjects = Subject.objects.all()
    calendar = AcademicCalendarEntry.objects.all()[:12]
    results = AcademicResult.objects.all()[:6]
    context = {
        'departments': departments,
        'programs': programs,
        'subjects': subjects,
        'calendar': calendar,
        'results': results,
    }
    return render(request, 'vision/academics.html', context)


def admissions_apply(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save()
            return redirect('vision:admissions_success')
    else:
        form = AdmissionForm()
    context = {'form': form}
    return render(request, 'vision/admissions/apply.html', context)


def admissions_success(request):
    return render(request, 'vision/admissions/success.html')


def student_life(request):
    clubs = Club.objects.all()
    activities = Activity.objects.all().order_by('-date')
    sports = SportTeam.objects.all()
    council = StudentCouncilMember.objects.all()
    discipline = DisciplinePolicy.objects.first()
    counseling = CounselingResource.objects.all()
    transport = TransportRoute.objects.all()
    context = {
        'clubs': clubs,
        'activities': activities,
        'sports': sports,
        'council': council,
        'discipline': discipline,
        'counseling': counseling,
        'transport': transport,
    }
    return render(request, 'vision/student_life.html', context)


def parents(request):
    notices = ParentNotice.objects.all()[:10]
    context = {'notices': notices}
    return render(request, 'vision/parents.html', context) 
