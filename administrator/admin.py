from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(category_Course)
admin.site.register(Video)