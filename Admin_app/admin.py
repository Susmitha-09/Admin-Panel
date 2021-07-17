from django.contrib import admin
from Admin_app.models import rider,driver,ride
# Register your models here.
class riderAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','email']
    search_fields = ['first_name']

class driverAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','email']
    search_fields = ['first_name']

class rideAdmin(admin.ModelAdmin):
    fields = ['first_name','date','url']
    search_fields = ['first_name','date']

admin.site.register(rider,riderAdmin)
admin.site.register(driver,driverAdmin)
admin.site.register(ride,rideAdmin)
