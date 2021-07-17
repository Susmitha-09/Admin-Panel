from django.shortcuts import render
import pyrebase
from django.http import HttpResponse
from Admin_app.models import rider,driver,ride

config={
    "apiKey": "AIzaSyBl6lRCLLfwu7y4hTaiS1PFb1SKoqGh7wE",
    "authDomain": "adminpanelproject-1ed1c.firebaseapp.com",
    "databaseURL": "https://adminpanelproject-1ed1c-default-rtdb.firebaseio.com",
    "projectId": "adminpanelproject-1ed1c",
    "storageBucket": "adminpanelproject-1ed1c.appspot.com",
    "messagingSenderId": "932122587260",
    "appId": "1:932122587260:web:a8a4de8c152c1fdb2499f9",
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.

def index(request):
    rider_first_name = database.child('rider').child('first_name').get().val()
    rider_last_name = database.child('rider').child('last_name').get().val()
    rider_email = database.child('rider').child('email').get().val()
    driver_first_name = database.child('driver').child('first_name').get().val()
    driver_last_name = database.child('driver').child('last_name').get().val()
    driver_email = database.child('driver').child('email').get().val()
    driver_phone_number = database.child('driver').child('phone_number').get().val()


    return render(request,'Admin_app/index.html',{
        "rider_first_name": rider_first_name,
        "rider_last_name": rider_last_name,
        "rider_email": rider_email,
        "driver_first_name": driver_first_name,
        "driver_last_name": driver_last_name,
        "driver_email": driver_email,
        "driver_phone_number": driver_phone_number
    })

def riders(request):

    rider_list = rider.objects.order_by('first_name')
    rider_dict = {"riders":rider_list}
    return render(request,'Admin_app/riders.html',context=rider_dict)
