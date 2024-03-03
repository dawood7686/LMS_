"""SoftUI_LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from lms import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('login/', views.loginn, name="login"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/profile/', views.lms_profile, name="lms_courses"),
    path('dashboard/', views.lms_dashboard, name="lms_dashboard"),
    path('dashboard/<int:id>', views.lms_dashboard_filter, name="lms_dashboard"),
    path('dashboard/progress/', views.lms_progress, name="lms_progress"),
    path('dashboard/billing/', views.lms_billing, name="lms_billing"),
    path('logout/', views.log_out, name="logout"),
    path('dashboard/<str:id>/slides/', views.course_dash, name="course Slides"),
    path('dashboard/slides/<str:id>/<str:number>', views.course_dashboard, name="course Slides"),
    path('dashboard/quiz/<str:name>/<str:number>', views.course_quiz, name="course Quiz"),
    path('dashboard/quiz/start/<str:name>/<str:number>', views.take_quiz, name="course Quiz"),
    path('dashboard/finish/<str:name>/<str:number>', views.finish, name="course Quiz"),
    path('dashboard/community', views.community, name="course community"),
    path('certificate/<int:id>', views.user_certificate, name="certificate"),
    
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()    
handle404 = views.handle_404
handle302 = views.handle_302
handle500 = views.handle_500