from operator import irshift
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import *

# Create your models here.
class StudentList(models.Model):
    option_college = (('College of Agriculture', 'College of Agriculture'), ('College of Arts and Sciences', 'College of Arts and Sciences'), ('College of Computer Studies', 'College of Computer Studies'), ('College of Engineering', 'College of Engineering'), ('College of Nursing', 'College of Nursing'), ('School of Business and Management', 'School of Business and Management'), ('College of Education', 'College of Education'))
    option_year = (('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('5th Year', '5th Year'))
    option_sex = (('Female', 'Female'), ('Male', 'Male'))
    option_relationship = (('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), 
    ('Grandfather', 'Grandfather'), ('Grandmother', 'Grandmother'), ('Foster Parent', 'Foster Parent'), 
    ('Step-Parent', 'Step-Parent'), ('Step-Sibling', 'Step-Sibling'), ('Guardian', 'Guardian'))
    option_status = (('PENDING', 'PENDING'), ('ADMITTED', 'ADMITTED'), ('REJECTED', 'REJECTED'))

    # Student Information
    exam_number = models.CharField(primary_key = True, max_length = 5, verbose_name = 'Exam Number', validators = [validate_exam_number])
    name = models.CharField(max_length = 50, verbose_name = 'Name:', validators = [validate_names, validate_name_format], help_text = 'Follow this format: LastName, FirstName MiddleName')
    sex = models.CharField(max_length = 10, choices = option_sex)
    birthdate = models.DateField(verbose_name= 'Birthdate', help_text = 'Follow this format: YYYY-MM-DD')
    country = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    home_address = models.CharField(max_length = 50, verbose_name = 'Home Address')
    contact_number = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(9000000000)], verbose_name = 'Contact Number (+63)')
    email = models.EmailField()
    college = models.CharField(max_length = 50, choices = option_college)
    course = models.CharField(max_length = 50, verbose_name = 'Program')
    year = models.CharField(max_length = 8, choices = option_year, verbose_name = 'Year Level')
    high_school = models.CharField(max_length = 50, verbose_name = 'High School', validators = [validate_names])
    school_address = models.CharField(max_length = 50, verbose_name = 'School Address')
    gpa = models.DecimalField(default = 0.00, max_digits = 3, decimal_places = 2, validators=[MaxValueValidator(4.00), MinValueValidator(0.00)], verbose_name = 'GPA')
    enrolment_status = models.CharField(default = 'PENDING', choices = option_status, max_length = 10, verbose_name = 'Enrolment Status')
    date_created = models.DateTimeField(auto_now_add = True, verbose_name = 'Date Applied')
    # Parent/Guardian
    steward_name = models.CharField(max_length = 50, verbose_name = 'Name', validators = [validate_names, validate_name_format], help_text = 'Follow this format: LastName, FirstName MiddleName')
    steward_sex = models.CharField(max_length = 10, verbose_name = 'Sex', choices = option_sex)
    steward_relationship = models.CharField(max_length = 20, choices = option_relationship, verbose_name = 'Relationship')
    steward_country = models.CharField(max_length = 50, verbose_name = 'Country')
    steward_city = models.CharField(max_length = 50, verbose_name = 'City')
    steward_home_address = models.CharField(max_length = 50, verbose_name = 'Home Address')
    steward_contact_number = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(9000000000)], verbose_name = 'Contact Number (+63)')
    steward_email = models.EmailField(verbose_name = 'Email')
    # Previous University
    if_transferee = models.BooleanField(default = False, verbose_name = 'If Transferee')
    uni_name = models.CharField(max_length = 50, verbose_name = 'Name', null = True, blank = True, validators = [validate_names])
    uni_country = models.CharField(max_length = 50, verbose_name = 'Country', null = True, blank = True)
    uni_city = models.CharField(max_length = 50, verbose_name = 'City', null = True, blank = True)
    uni_address = models.CharField(max_length = 50, verbose_name = 'University Address', null = True, blank = True)
    uni_college = models.CharField(max_length = 20, verbose_name = 'Previous College', null = True, blank = True, validators = [validate_names])
    uni_course = models.CharField(max_length = 50, verbose_name = 'Previous Program', null = True, blank = True, validators = [validate_names])
    uni_year = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], verbose_name = 'Previous Year', null = True, blank = True)
    uni_reason = models.TextField(verbose_name = 'Reason of Transfer', null = True, blank = True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.steward_name = self.steward_name.title()
        self.home_address = self.home_address.capitalize()
        self.high_school = self.steward_name.title()
        self.school_address = self.home_address.capitalize()
        self.steward_home_address = self.steward_home_address.capitalize()
        if not self.uni_name is None:
            self.uni_name = self.uni_name.title()
        if not self.uni_address is None:
            self.uni_address = self.uni_address.capitalize()
        if not self.uni_college is None:
            self.uni_college = self.uni_college.title()
        if not self.uni_course is None:
            self.uni_course = self.uni_course.title()
        if not self.uni_reason is None:
            self.uni_reason = self.uni_reason.capitalize()
        super().save(*args, **kwargs)

    class Meta:
        #To change the name in the List of Admin Panel
        verbose_name = 'Student'