from django.contrib import admin
from . models import User,UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class customUseradmin(UserAdmin): #making password non editable in admin panel
    list_display = ('email','username','first_name','last_name','role') #to display in admin panel
    ordering = ('-date_joined',) # - means descendng order
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User)
admin.site.register(UserProfile)