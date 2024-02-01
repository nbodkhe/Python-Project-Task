from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.URLField(blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    email_verification_token = models.CharField(max_length=255, blank=True, null=True)
    cm_firebase_token = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    order_count = models.IntegerField()
    emp_id = models.CharField(max_length=20)
    department_id = models.IntegerField()
    is_veg = models.BooleanField(default=False)
    is_sat_opted = models.BooleanField(default=False)
    device_id = models.CharField(max_length=255)
    is_invalid_device = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    breakfast = models.CharField(max_length=20, blank=True, null=True)
    lunch = models.CharField(max_length=20, blank=True, null=True)
    dinner = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.date
