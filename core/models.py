from django.db import models
from account.models import CustomUser


class TimeStampModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="automaticaly set when model created")
    updated_at = models.DateTimeField(auto_now=True, help_text="automaticaly updated when model saved")

    class Meta:
        abstract = True


class UserTimeStampModelMixin(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                                   related_name="%(class)s_created", 
                                   help_text="user who created this record",
                                   null=True,
                                   blank=True
                                   )
    updated_by = models.ForeignKey(CustomUser, 
                                   on_delete=models.CASCADE, 
                                   related_name="%(class)s_updated",
                                   help_text="user who last update this record",
                                   null=True,
                                   blank=True
                                   )
    class Meta:
        abstract = True
    