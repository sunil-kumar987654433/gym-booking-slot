import uuid
from django.db import models
from core.models import TimeStampModelMixin, UserTimeStampModelMixin
from account.models import CustomUser

class Instructor(TimeStampModelMixin):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user_instructor = models.OneToOneField(CustomUser, help_text="Instructor", on_delete=models.SET_NULL, null=True )
    father_name = models.CharField(max_length=50, help_text="name of father of instructor.")
    contact_number = models.CharField(max_length=20, help_text="contact number of instructor.")
    full_address = models.TextField(help_text="full address of Instructor.")
    zip_code = models.CharField(max_length=10, help_text="zip code of Instructor local area.")
    experience = models.PositiveSmallIntegerField(default=0, help_text="month of experience.")

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"



class FitnessClass(TimeStampModelMixin):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    class_name = models.CharField(max_length=255, help_text="name of fitness class category i.e Yoga, Zumba, and HIIT.")
    description = models.TextField(help_text="short description of the fitness class.")
    instructer = models.ManyToManyField(Instructor, help_text="Instructors assigned to this fitness class.")
    from_date = models.DateField(help_text="start date of fitness class")
    to_date = models.DateField(help_text="end date of fitness class")
    from_time = models.TimeField(help_text="start time of fitness class")
    to_time = models.TimeField(help_text="end time of fitness class")
    available_slot = models.PositiveSmallIntegerField(default=0, help_text="Number of available slots.")

    class Meta:
        verbose_name = "Fitness Class"
        verbose_name_plural = "Fitness Classes"


class BookingSlot(TimeStampModelMixin):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(CustomUser, help_text="Client for fitness slot.", on_delete=models.SET_NULL, null=True)
    fitness_class = models.ManyToManyField(FitnessClass ,help_text="fitness class for client.")

    class Meta:
        verbose_name = "Booking Slot"
        verbose_name_plural = "Booking Slots"
        


