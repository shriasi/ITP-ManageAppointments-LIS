from django.db import models  
class Appointments(models.Model):  
    Appoint_ID = models.CharField(max_length=20)  
    Ap_Cus_name = models.CharField(max_length=200)  
    Ap_Cus_address = models.CharField(max_length=200) 
    Ap_Cus_email = models.EmailField()
    Ap_Purpose = models.CharField(max_length=200)
    Ap_Notes = models.CharField(max_length=200)
    Ap_Date_time = models.DateTimeField(default='2015-05-11 13:01:01')
    Ap_Venue = models.CharField(max_length=200)
    class Meta:  
        db_table = "App_details" 
