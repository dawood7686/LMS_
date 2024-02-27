from django.shortcuts import render, redirect, HttpResponse
from .models import user, course, community_Feature, Course_Enrollment, website, front_page, categories, video, slides, Quiz, country, progress
from django.contrib.auth.models import User
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,  login, logout
from .certificates import generate_certificate
# from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_exempt



def index(request):
     # print(request.user +'  user')
     user = str(request.user)
     if user == "AnonymousUser":
          return redirect('/login')
     else:
#     return render(request, 'mainpage.html')
          return redirect("/dashboard")

def loginn(request):
    email=None
    password=None
    error_msg = None
    if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                return redirect("/dashboard")
            else:
                error_msg='''Invalid credentials! Please try again'''
    print(error_msg, email, password)
    return render(request, "login.html", {'error':error_msg})

def signup(request):
     countries = country.objects.all()
     error_msg=None
     if request.method == 'POST':
          firstname = request.POST['firstname']
          lastname = request.POST['lastname']
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          confirm_password = request.POST['confirm_password']
          job_role = request.POST['job_role']
          state = request.POST['state']
          company = request.POST['Company']
          country_id = request.POST['country']
          country_detail = country.objects.get(code=country_id)
          print(firstname, lastname, email, password, confirm_password, job_role, state, company)
          if len(firstname)<=2 or len(lastname)<=2 or len(username)<=3:
            error_msg="Please enter the correct name!"
          elif len(password)>=8:
               if password==confirm_password:
                    pre_user = User.objects.filter(username=username).exists()
                    if pre_user:
                         error_msg = '''Username is already exist''' 
                    else:
                         user1 = user(Name=f"{firstname} {lastname}", username=username, Email=email, Password=password, job_role=job_role, state=state, company=company, Country=country_detail)
                         user1.save()
                         users = User.objects.create_user(username, email, password)
                         users.first_name=firstname
                         users.last_name=lastname
                         users.save()
                         
                         return redirect("/login")
               else:
                    error_msg = '''Incorrect password in Confirm password.'''
          else:
               error_msg='''Passwords doesn't match'''
     print(error_msg)
     return render(request, 'signup.html', {"error":error_msg, 'countries':countries})


def lms_profile(request):
     details = {}
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     if detail:
          details = {'details':detail[0],
                     'website':website_data[0]}
     else:
          return redirect('/login/')
     return render(request, 'user.html', details)

def lms_dashboard(request):
     details = {}
     users = request.user
     detail = user.objects.filter(username=users)
     enrollment = course.objects.all()
     category = categories.objects.all()
     print(request)
     website_data = website.objects.filter(code = detail[0].Country)
     if detail:
          if enrollment:
               details = {
                    'details':detail[0],
                    'website':website_data[0],
                    'courses':enrollment,
                    'Category':category,
                    }
          else:
               details = {'details':detail[0],
                    'website':website_data[0],}
     else:
          return redirect('/login/')
     return render(request, 'dashboard.html', details)

def lms_dashboard_filter(request, id):
     details = {}
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     enrollment = course.objects.filter(category=id)
     category = categories.objects.all()
     if detail:
          if enrollment:
               for i in category:
                    print(i)
               details = {
                    'details':detail[0],
                    'website':website_data[0],
                    'courses':enrollment,
                    'Category':category,
                    }
          else:
               details = {'details':detail[0],
                    'website':website_data[0],}
     else:
          return redirect('/login/')
     return render(request, 'dashboard.html', details)

def lms_progress(request):
     details = {}
     data = []
     percentage = {}
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     complete_progress = progress.objects.filter(User = users)
     if detail:
          for i in complete_progress:
               slide = slides.objects.filter(Course = i.Course)
               for slid in slide:
                    data.append(slid.Slide_Number)
               print(len(data))
               percent = int((i.Slide * 100) / len(data))
               print(percent)
               percentage[i.Course.Name] = percent
               print(percentage)
               data=[]
                    
          details = {'details':detail[0],
                     'website':website_data[0],
                     'progress':complete_progress,
                     'percentage':percentage,
                     }
     else:
          return redirect('/login/')
     return render(request, 'progress.html', details)

def lms_billing(request):
     details = {}
     users = request.user
     detail = user.objects.filter(username=users)
     website_data=website.objects.all()
     if detail:
          details = {'details':detail[0], 
                     'website':website_data[0]}
     else:
          return redirect('/login/')
     return render(request, 'payment.html', details)

def log_out(request):
     logout(request)
     return redirect('/')

def quiz(request):
     if request.method == "POST":
          option_A = str(request.POST['1'])
          if option_A:
               print(option_A)
     details = {}
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     if detail:
          details = {'details':detail[0],
                     'website':website_data[0]}
     else:
          return redirect('/login/')
     return redirect('/dashboard/1/quiz')

def course_dash(request, id):
     users = request.user
     detail = User.objects.get(username=users)
     courses = course.objects.get(id=id)
     slide = slides.objects.filter(Course = courses)
     data = progress.objects.filter(User=users, Course = courses.id)
     if data:     
          print(f"{data[0].Slide} _________________")
          try:
               slide = slides.objects.get(Course = courses, Slide_Number=data[0].Slide)
          
               return redirect(f'/dashboard/slides/{courses.Name}/{slide.Slide_Number}')
          except:
               return redirect(f'/')
     else:
          course_progress = progress(User=detail, Course=courses, Slide=1, Status="In-Progress")
          course_progress.save()
          return redirect(f'/dashboard/slides/{courses.Name}/{slide[0].Slide_Number}')
     
     # return render(request, 'Course_slides.html')
@xframe_options_exempt
def course_dashboard(request, number, id):
     details = {}
     slidess = []
     # request.headers['Content-Security-Policy']='default-src \'self\''
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     courses = course.objects.get(Name=id)
     slide = slides.objects.filter(Course = courses)
     progres = progress.objects.filter(Course = courses, User=users)
     update = progress.objects.get(id=progres[0].id)
     selected = slides.objects.filter(Course = courses, Slide_Number=number)
     try:
          selected = slides.objects.filter(Course = courses, Slide_Number=number)

          if detail:
               import zipfile
               import os
               if os.path.exists((f'{os.getcwd()}/lms/static/uploads/{id}({number})/story.html')) and os.path.isdir((f'{os.getcwd()}/lms/static/uploads/{id}({number})/story.html')):  
                         path = f'uploads/{id}({number})/story.html'
                         print(path)
                         
               else:
                    with zipfile.ZipFile(f'{os.getcwd()}/media/{selected[0].Slide}', 'r') as zip_ref:
                         zip_ref.extractall(f'{os.getcwd()}/lms/static/uploads/{id}({number})')
                         path = f'uploads/{id}({number})/story.html'
                    # return redirect("/media/uploads/ch1/story.html")
               print(path)
               if update.Slide < int(number):
                    update.Slide = int(number)
               print(update.Slide)
               for i in slide:
                    slidess.append(i.Slide_Number)
               percentage = int((int(update.Slide) * 100) / len(slidess))
               print(percentage)
               if percentage != 100:
                    update.Status = "In-Progress"
               else:
                    update.Status = "Completed"
               print(percentage)
               slidess = []
               update.percentage = percentage
               update.save()
               details = {'details':detail[0],
                         'website':website_data[0],
                         'slides':slide,
                         'selected':selected[0],
                         'path': path,
                         'next':f'/dashboard/quiz/{courses.Name}/{int(number)}',
                         'slide_number':f'/dashboard/slides/{courses.Name}',
                         'percentage':percentage,
                         }
          else:
               return redirect('/login/')
     except:
          
          update.Status = "Completed"
          update.percentage = 100
          update.save()
          print(update.Status)
          return redirect(f'/dashboard/finish/{id}/{update.Slide}')
          # return redirect('/dashboard/progress')
          
     return render(request, 'course_slides.html', details)

def course_quiz(request, name, number):
     print(name)
     details = {}
     quiz_ids=[]
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     courses = course.objects.get(Name=name)
     slide = slides.objects.filter(Course = courses)
     quiz = Quiz.objects.filter(Course = courses, After = number)
     selected = slides.objects.filter(Course = courses, Slide_Number=number)
     if detail:
          if quiz:
               details = {'details':detail[0],
                         'website':website_data[0],
                         'slides':slide,
                         'selected':selected[0],
                         'next':f'/dashboard/quiz/start/{courses.Name}/{int(number)}',
                         'slide_number':f'/dashboard/slides/{courses.Name}',
                         'quiz':quiz,
                         }
          else:
               return redirect(f'/dashboard/slides/{courses.Name}/{int(number)+1}')
     else:
          return redirect('/login/')
     return render(request, "ready_quiz.html", details)
def finish(request, name, number):
     print(name)
     details = {}
     quiz_ids=[]
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     courses = course.objects.get(Name=name)
     slide = slides.objects.filter(Course = courses)
     quiz = Quiz.objects.filter(Course = courses, After = number)
     selected = slides.objects.filter(Course = courses, Slide_Number=number)
     if detail:
               details = {'details':detail[0],
                         'website':website_data[0],
                         'slides':slide,
                         'selected':selected[0],
                         'next':f'/dashboard/quiz/start/{courses.Name}/{int(number)}',
                         'slide_number':f'/dashboard/slides/{courses.Name}',
                         "finish":f'/dashboard/finish/{courses.Name}/{int(number)}',
                         }
     else:
          return redirect('/login/')
     return render(request, "finish.html", details)


def take_quiz(request, name, number):
     print(name)
     details = {}
     quiz_ids=[]
     result = {}
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     courses = course.objects.get(Name=name)
     slide = slides.objects.filter(Course = courses)
     quiz = Quiz.objects.filter(Course = courses, After = number)
     selected = slides.objects.filter(Course = courses, Slide_Number=number)
     if detail:
          if quiz:
               for i in quiz:
                    quiz_ids.append(i.id)
                    if len(quiz)==10:
                         break
               # print(quiz_ids)
               details = {'details':detail[0],
                         'website':website_data[0],
                         'slides':slide,
                         'selected':selected[0],
                         'next':f'/dashboard/quiz/{courses.Name}/{int(number)}',
                         'slide_number':f'/dashboard/slides/{courses.Name}',
                         'quiz':quiz,
                         'ids':quiz_ids,
                         'slide_next':f'/dashboard/slides/{courses.Name}/{int(number)+1}'
                         }
          else:
               return redirect(f'/dashboard/slides/{courses.Name}/{int(number)+1}')
     else:
          return redirect('/login/')
     sol = []
     if request.method == "POST":
          for i in quiz_ids:
               m = str(request.POST[f'{i}'])
               print(m)
               ans = Quiz.objects.get(id=i)
               print(ans, '_________________________ans')
               if m == ans.correct_option:
                    print(1)
                    result[f"{ans.id}"] = 1
                    sol.append(1)
               else:
                    print(0)
                    result[f"{ans.id}"] = 0

               
               details['result'] = (f'{(len(sol)*100)/len(quiz_ids)}')
               print(details['result'])
                    
          return render(request, "ending_page.html", details)
     return render(request, "course_quizs.html", details)

# def course_quiz(request, name, number):
#      print(name)
#      details = {}
#      quiz_ids=[]
#      users = request.user
#      detail = user.objects.filter(username=users)
#      website_data = website.objects.filter(code = detail[0].Country)
#      courses = course.objects.get(Name=name)
#      slide = slides.objects.filter(Course = courses)
#      quiz = Quiz.objects.filter(Course = courses, After = number)
#      selected = slides.objects.filter(Course = courses, Slide_Number=number)
#      if detail:
#           if quiz:
#                for i in quiz:
#                     quiz_ids.append(i.id)
#                     if i.id == quiz_ids[0]:
#                          print(i.id)
                    
#                     if len(quiz)==10:
#                          break
#                print(quiz_ids)
#                details = {'details':detail[0],
#                          'website':website_data[0],
#                          'slides':slide,
#                          'selected':selected[0],
#                          'next':f'/dashboard/quiz/{courses.Name}/{int(number)}',
#                          'slide_number':f'/dashboard/slides/{courses.Name}',
#                          'quiz':quiz,
#                          'ids':quiz_ids
#                          }
#           else:
#                return redirect(f'/dashboard/slides/{courses.Name}/{int(number)+1}')
#      else:
#           return redirect('/login/')
#      if request.method == "POST":
#           for i in quiz_ids:
#                m = str(request.POST[f'{i}'])
#                ans = Quiz.objects.get(id=i)
#                if m == ans.correct_option:
#                     print(1)
#                else:
#                     print(0)
                    
#           return redirect(f'/dashboard/slides/{courses.Name}/{int(number)+1}')
#      return render(request, "course_quizs.html", details)

def community(request):
     if request.method == "POST":
          message = request.POST['message']
          if message=="":
               pass
          else:
               name = User.objects.get(username = request.user)
               user_message = community_Feature(Name = name, comments = message)
               user_message.save()
     details = {}
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     all_messages = community_Feature.objects.all()
     if detail:
          details = {'details':detail[0],
                     'website':website_data[0],
                     'messages':all_messages}
     else:
          return redirect('/login/')
     return render(request, "course_community.html", details)



def user_certificate(request, id):
     users = request.user
     detail = user.objects.filter(username=users)
     website_data = website.objects.filter(code = detail[0].Country)
     course_name = progress.objects.get(id=id)
     if course_name:
          if course_name.Status=="Completed":
               for i in website_data:
                    print(i.logo)
               print(course_name.Course)
               from django.http import FileResponse
               certificate = generate_certificate(detail[0].Name, course_name.Course.Name, '23-8-2023', website_data[0].logo)
               print(certificate)
               # response = FileResponse(certificate, content_type='image/jpeg')
               # response['Content-Disposition'] = f'attachment; filename="admin_certificate.png"'

               return redirect(f'/static/{certificate}')
               # response =  HttpResponse(content_type='application/pdf')
               # response['Content-Disposition'] = f'D:/LMS/project/SoftUI_LMS/lms/static; filename="admin_certificate.png"'
               # return redirect('/dashboard/progress/')
               # return response

def handle_404(request, exception):
     request.status_code = 404
     return render(request, "404.html")