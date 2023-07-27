from django.contrib import admin
from . models import manager


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','username','password')

admin.site.register(manager,ManagerAdmin)




