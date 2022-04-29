
from tkinter import Widget
from django.contrib.auth.models import User
from django import forms
from testapp.models import Resume,job

class RegistrationUser(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')

        widgets={
            "username":forms.TextInput(attrs={"class":'form-control col-xs-4'}),
            "password":forms.TextInput(attrs={"class":'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "first_name":forms.TextInput(attrs={"class":'form-control'}),
            "last_name":forms.TextInput(attrs={"class":'form-control'}),

        }

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]
WORK_STATUS=[
    ('Fresher','Fresher'),
    ('Experiance','Experiance')
]
JOB_CITY_CHOICES=[
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Banglore','Banglore'),
    ('Kerala','Kerala'),
]

class jobForm(forms.ModelForm):
    class Meta:
        model=job
        fields=['Jtitle','cname',"Jquali","Jloacation","Jsalary"]

       
    
class ResumeForm(forms.ModelForm):
# For creating gender in radio format & job city in Check Box 
    gender =forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    work_details=forms.ChoiceField(choices=WORK_STATUS,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(choices=JOB_CITY_CHOICES,widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model=Resume
        fields=['job_desc','comp_name','name','dob','gender','education','college_name','state','city','pin','mobile','email','work_details','job_city','my_file','profile_image']

    # change form name
        labels={"job_desc":"Applying For","comp_name":"Company Name","name":"Full Name","dob":"Date of Birth","gender":"Gender","education":"Education Details","college_name":"College Name","city":"Current-City","pin":"Pin Code","state":"State","mobile":"Mobile Number","email":"Email Id","work_details":"Work Status","job_city":"Desired Job Location","my_file":"Documents","profile_image":"Profile Image"}

    # How to add bootstraps to form field
        widgets={
            "job_desc":forms.TextInput(attrs={"class":'form-control'}),
            "comp_name":forms.TextInput(attrs={"class":'form-control'}),
            "name":forms.TextInput(attrs={"class":'form-control'}),
            "dob":forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            "education":forms.Select(attrs={'class':'form-select'}),
            "college_name":forms.TextInput(attrs={'class':'form-control'}),
            "city":forms.TextInput(attrs={'class':'form-control'}),
            "pin":forms.NumberInput(attrs={'class':'form-control'}),
            "state":forms.Select(attrs={'class':'form-select'}),
            "mobile":forms.NumberInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            
        }