from django.urls import path
from django.contrib import admin
from Admin_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.riders,name='riders'),
]
