from django.db import models

class SiteInfo(models.Model):
    school_name = models.CharField(max_length=200, default="Kisoro Vision Secondary School")
    motto = models.CharField(max_length=255, blank=True, default="Knowledge, Integrity, Service")
    principal_name = models.CharField(max_length=100, blank=True)
    principal_message = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    admissions_open = models.BooleanField(default=False)

    def __str__(self):
        return self.school_name


class QuickLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.title} ({self.date})"


class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    summary = models.TextField(blank=True)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.author} - {self.role}"


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.title} ({self.year})"


class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    qualifications = models.TextField(blank=True)
    subjects = models.ManyToManyField('Subject', blank=True)
    hire_date = models.DateField(null=True, blank=True)
    public_profile = models.BooleanField(default=True)
    cv = models.FileField(upload_to='staff_cvs/', blank=True, null=True)
    professional_development = models.TextField(blank=True)
    is_leadership = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.role}"


class Facility(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)

    def __str__(self):
        return self.name


class AboutPage(models.Model):
    overview = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    values = models.TextField(blank=True)
    history = models.TextField(blank=True)
    accreditations = models.TextField(blank=True)
    infrastructure = models.TextField(blank=True)
    principal = models.ForeignKey(StaffMember, on_delete=models.SET_NULL, null=True, blank=True, related_name='principal_profile')

    def __str__(self):
        return "About Page"


class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    LEVEL_CHOICES = [
        ('KG', 'Kindergarten / Primary'),
        ('MS', 'Middle School'),
        ('HS', 'High School'),
    ]
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    overview = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    programs = models.ManyToManyField(Program, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AcademicCalendarEntry(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    details = models.TextField(blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.title} ({self.date})"


class AcademicResult(models.Model):
    year = models.PositiveIntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.program.name} - {self.year}"


class AdmissionApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]
    applicant_name = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True)
    document = models.FileField(upload_to='admissions/', blank=True, null=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.applicant_name} -> {self.student_name} ({self.get_status_display()})"


class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('CLUB', 'Club/Society'),
        ('EVENT', 'Event'),
        ('SPORT', 'Sport'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    details = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class SportTeam(models.Model):
    name = models.CharField(max_length=200)
    coach = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class StudentCouncilMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


class DisciplinePolicy(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Discipline Policy"


class CounselingResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    contact = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class TransportRoute(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ParentNotice(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='notices/', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} ({self.date})"
