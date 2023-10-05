from django.contrib import admin

# Register your models here.
from .models import user, course, website, community_Feature, categories, Course_Enrollment, front_page, country, Quiz, video, slides, progress

class courseAdmin(admin.ModelAdmin):
    list_display = ['Name', 'price']
admin.site.register(course, courseAdmin)

class userAdmin(admin.ModelAdmin):
    list_display = ['Name', 'state']
admin.site.register(user, userAdmin)

class websiteAdmin(admin.ModelAdmin):
    list_display = ['Name']
admin.site.register(website, websiteAdmin)

class communityAdmin(admin.ModelAdmin):
    list_display = ['Name']
admin.site.register(community_Feature, communityAdmin)

class categoriesAdmin(admin.ModelAdmin):
    list_display = ['category']
admin.site.register(categories, categoriesAdmin)


admin.site.register(Course_Enrollment)
admin.site.register(front_page) 
admin.site.register(slides) 
admin.site.register(video) 
admin.site.register(Quiz) 
admin.site.register(country) 
admin.site.register(progress) 
