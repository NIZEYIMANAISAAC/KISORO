from django.contrib import admin
from .models import SiteInfo, QuickLink, Event, News, Testimonial, Achievement, StaffMember, Facility, AboutPage, Department, Program, Subject, AcademicCalendarEntry, AcademicResult, AdmissionApplication, Club, Activity, SportTeam, StudentCouncilMember, DisciplinePolicy, CounselingResource, TransportRoute, ParentNotice


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'motto', 'contact_email', 'admissions_open')


@admin.register(QuickLink)
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')
    ordering = ('order',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_featured')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'role')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'is_leadership')


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')


@admin.register(AcademicCalendarEntry)
class AcademicCalendarEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


@admin.register(AcademicResult)
class AcademicResultAdmin(admin.ModelAdmin):
    list_display = ('program', 'year')


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'student_name', 'program', 'status', 'submitted_at')
    list_filter = ('status', 'program')
    readonly_fields = ('submitted_at',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')


@admin.register(SportTeam)
class SportTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'coach')


@admin.register(StudentCouncilMember)
class StudentCouncilMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'year')


@admin.register(DisciplinePolicy)
class DisciplinePolicyAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(CounselingResource)
class CounselingResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact')


@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ParentNotice)
class ParentNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date') 
