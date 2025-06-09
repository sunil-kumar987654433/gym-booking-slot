from django.contrib import admin
from book.models import Instructor, BookingSlot, FitnessClass
# Register your models here.

admin.site.register(( BookingSlot, FitnessClass))


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', "user_instructor", "user_instructor_name", "user_instructor_email", "experience"]
    search_fields = ['user_instructor_email', ]


    def user_instructor_email(self, obj):
        return f"{obj.user_instructor.email}"
    
    def user_instructor_name(self, obj):
        return f"{obj.user_instructor.first_name}"