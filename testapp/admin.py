from django.contrib import admin
from testapp.models import Resume,job
# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display=['job_desc','comp_name','name','dob','gender','education','college_name','city','pin','state','mobile','email','work_details','job_city','my_file',"profile_image"]
admin.site.register(Resume,ResumeAdmin)

class jobAdmin(admin.ModelAdmin):
    list_display=['Jtitle','cname','Jquali','Jloacation','Jsalary']
admin.site.register(job,jobAdmin)