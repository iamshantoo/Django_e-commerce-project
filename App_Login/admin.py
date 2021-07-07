from django.contrib import admin
from App_Login.models import User, Profile

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.site_header = 'E-Shop Administration'