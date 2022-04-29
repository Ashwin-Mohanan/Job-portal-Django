"""Resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include

from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf.urls.static import static #------- for uploading image from data base
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),

    path("",views.homeView.as_view()),
    path("job/",views.jobView.as_view()),
    path("form/",views.ResumeView.as_view(),name="forms"),
    # path('filter/',views.filter_job,name="filter"),
    path('reg/', views.registration_view),
    path('logout/', views.logout_view),
    
    path("<int:pk>",views.CandidateView.as_view(),name='candi'), #-----to see who all have applyied candidate details

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #------- for uploading image from data base
