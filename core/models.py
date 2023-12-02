from django.db import models



class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    Age = models.IntegerField(max_length=3)
    insurance_id= models.CharField(max_length=50, blank=True, null=True)
    is_insurance_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Doctor(models.Model):
    name =models.CharField(max_length=100)
    speciality =models.CharField(max_length=100)
    
class Appointment(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time=models.DateTimeField

