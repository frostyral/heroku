from django.contrib import admin, messages
from .models import StudentList
from django.utils.translation import ngettext

admin.site.index_title = 'Home'
admin.site.site_header = 'STSM Administration'
admin.site.site_title = 'Administration'

# Register your models here.
@admin.register(StudentList)
class StudentApplication(admin.ModelAdmin):
    # View Table
    list_display = ('exam_number', 'name', 'college', 'course', 'enrolment_status', 'date_created')
    list_editable = ('enrolment_status',)

    search_fields = ('exam_number', 'name', 'college', 'course', 'enrolment_status', 'date_created')
    readonly_fields = ('date_created',)
    ordering = ('date_created',)
    actions = ['make_admitted', 'make_pending', 'make_rejected']

    # These are the selection actions; Can be admit/reject/pend students in bulk
    @admin.action(description='Admit selected Students')
    def make_admitted(self, request, queryset):
        updated = queryset.update(enrolment_status='ADMITTED')
        self.message_user(request, ngettext(
            '%d student was admitted.',
            '%d students were admitted.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Pend selected Students')
    def make_pending(self, request, queryset):
        updated = queryset.update(enrolment_status='PENDING')
        self.message_user(request, ngettext(
            '%d student reverted back to pending.',
            '%d students reverted back to pending.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Reject selected Students')
    def make_rejected(self, request, queryset):
        updated = queryset.update(enrolment_status='REJECTED')
        self.message_user(request, ngettext(
            '%d student was rejected.',
            '%d students were rejected.',
            updated,
        ) % updated, messages.SUCCESS)

    list_filter = ('if_transferee', 'college', 'course', 'enrolment_status', 'date_created')

    # Add Form
    fieldsets = (
        ('Biographical Info', {
            'fields': ('exam_number', ('name', 'sex',), 'birthdate', ('country', 'city',), 'home_address', ('email', 'contact_number',),)
        }),
        ('Educational Background', {
            'fields': ('high_school', 'school_address', 'gpa',),
            'classes': ('collapse',),
        }),
        ('Parent/Guardian', {
            'fields': (('steward_name', 'steward_sex',), 'steward_relationship', ('steward_country', 'steward_city',), 'steward_home_address', ('steward_email', 'steward_contact_number',),),
            'classes': ('collapse',),
        }),
        ('Previous University', {
            'fields': ('if_transferee', 'uni_name', 'uni_country', 'uni_city', 'uni_address', 'uni_college', 'uni_course', 'uni_year', 'uni_reason',),
            'classes': ('collapse',),
        }),
        ('Submit Application', {
            'fields': ('college', 'course', 'year',),
            'classes': ('collapse',),
        }),
        ('Status', {
            'fields': ('enrolment_status',)
        }),
    )


