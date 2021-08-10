from django.db import models

# Create your models here.
class UserDetailsModel(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=170, blank=True, null=True)
    address = models.CharField(max_length=470, blank=True, null=True)
    lankmark = models.CharField(max_length=270, blank=True, null=True)
    mobile_no = models.BigIntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=270, blank=True, null=True)
    password = models.CharField(max_length=270, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "user_details"


class StatusModel(models.Model):
    status_id = models.AutoField(primary_key = True)
    status = models.CharField(max_length=170, blank=True, null=True)

    class Meta:
        db_table = "status_master"
