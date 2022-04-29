from distutils.command.upload import upload
import email
from turtle import title
from django.db import models

# Create your models here.
STATE_CHOICE =(
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh","Arunachal Pradesh"),("Assam","Assam"),("Bihar","Bihar"),("Chandigarh","Chandigarh"),("Chhattisgarh","Chhattisgarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Delhi","Delhi"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir","Jammu and Kashmir"),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Mizoram","Mizoram"),("Odisha","Odisha"),("Puducherry","Puducherry"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Tamil Nadu","Tamil Nadu"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),
)

EDUCATIONAL_DETAILS=[
    ("10","10"),
    ("12","12"),
    ("Bsc","Bsc"),
    ("Bsc(Computer Science)","Bsc(Computer Science)"),
    ("Bsc(I.T)","Bsc(I.T)"),
    ("MSC","MSC"),
    ("MCA","MCA"),
    ("B.com","B.com"),
    ("M.com","M.com"),
    ("BMS","BMS"),
    ("BBA","BBA"),
    
]
class job(models.Model):
    Jtitle=models.CharField(max_length=100)
    cname=models.CharField(max_length=100)
    Jquali=models.CharField(max_length=100)
    Jloacation=models.CharField(max_length=100)
    Jsalary=models.IntegerField()

class Resume(models.Model):
    job_desc=models.CharField(max_length=100,default='Any')
    comp_name=models.CharField(max_length=100,default='Any')
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    education=models.CharField(choices=EDUCATIONAL_DETAILS,max_length=100,default='none')
    college_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveBigIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    mobile=models.PositiveBigIntegerField()
    email=models.EmailField()
    work_details=models.CharField(max_length=100,default='none')
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)