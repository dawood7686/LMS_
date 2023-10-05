from django.db import models

from django.contrib.auth.models import User

class front_page(models.Model):
    description = models.TextField()
    Overview = models.TextField()
    def __str__(self):
        return "first page"
class categories(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField(default="")
    def __str__(self):
        return str(self.category)

class course(models.Model):
    Name = models.CharField(max_length=100)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    price = models.IntegerField()
    Description = models.TextField()
    Picture = models.ImageField(upload_to="media/")
    def __str__(self):
        return str(self.Name)
    
class Course_Enrollment(models.Model):
    Name = models.ForeignKey(User, on_delete=models.CASCADE)
    Course = models.ForeignKey(course, on_delete=models.CASCADE)
    Payment_Status = models.CharField(max_length=100)
    Completion_status = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Name)
    
class community_Feature(models.Model):
    Name = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()
    def __str__(self):
        return str(self.Name)
    
class country(models.Model):
    Country = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    def __str__(self):
        return str(self.Country)
    
class Quiz(models.Model):
    Course = models.ForeignKey(course, on_delete=models.CASCADE)
    Statement = models.TextField()
    option_A = models.CharField(max_length=20)
    option_B = models.CharField(max_length=20)
    option_C = models.CharField(max_length=20)
    option_D = models.CharField(max_length=20)
    correct_option = models.CharField(max_length=20)
    After = models.IntegerField(("After Which Slide"), default=1)
    
    def __str__(self):
        return str(self.Course)

class slides(models.Model):
    Course = models.ForeignKey(course, on_delete=models.CASCADE)
    Slide_Number = models.IntegerField()
    Slide = models.FileField(upload_to="media/")
    
    def __str__(self):
        return str(self.Course)

class video(models.Model):
    Course = models.ForeignKey(course, on_delete=models.CASCADE)
    Video_Number = models.IntegerField()
    Video_link = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.Course)

class website(models.Model):
    Name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='media/')
    code = models.ForeignKey(country, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Name)

class progress(models.Model):
    User = models.ForeignKey(User, verbose_name=("Progress"), on_delete=models.CASCADE)
    Course = models.ForeignKey(course, on_delete=models.CASCADE)
    Slide = models.IntegerField()
    Status = models.CharField(max_length=30)
    percentage = models.IntegerField(default=1)

    def __str__(self):
        return str(self.User)
    
    
class user(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    Country = models.ForeignKey(country, verbose_name=("Country"), on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Name)
