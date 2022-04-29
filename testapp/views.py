from django.http import HttpResponse
from testapp.forms import RegistrationUser
from django.shortcuts import render,redirect
from testapp.forms import ResumeForm
from testapp.models import Resume,job
from django.views import View
# from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

# from  django.contrib.auth.decorators import login_required ,permission_required

from django.views import View

# Create your views here.
class homeView(View):
    def get(self,request):
        return render(request,'testapp/home.html')
        
class jobView(View):
    def get(self,request):
        jobs=job.objects.all()
        return render(request,'testapp/job.html',{'jobs':jobs})


class ResumeView(LoginRequiredMixin,View):
    def get(self,request):
        forms=ResumeForm()
        candidate=Resume.objects.all()
        return render (request,'testapp/resume.html',{"candidates":candidate,"forms":forms})
    
    def post(self,request):
        forms=ResumeForm(request.POST, request.FILES)
        if forms.is_valid:
            forms.save()
            return redirect('/job')

# def filter_job(request):
#         if request.method=="POST":
#             name=request.POST.get('cname')
#             search=job.objects.all()
#             if name:
#                 search=job.objects.filter(cname__contains=name)
#             return render(request,'testapp/search_job.html',{"search":search})
#         elif request.method =="GET":
#             return render(request,'testapp/resume.html')
#         else:
#             return HttpResponse("ERROR")
            
class CandidateView(View):
    def get(self,request,pk):
        candi=Resume.objects.get(pk=pk)
        return render(request,"testapp/candidate.html",{"candi":candi})

def logout_view(request):
    return render(request,'testapp/logout.html')

def registration_view(request):
    reg=RegistrationUser()
    if request.method == 'POST':
        reg=RegistrationUser(request.POST)
        if reg.is_valid():
            user=reg.save();
            user.set_password(user.password)
            user.save()
            return redirect('/')
    return render(request,'testapp/register.html',{'reg':reg})