import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Admin_Panel.settings')

import django
# Import settings
django.setup()

# FAKE POPULATE
import random
from Admin_app.models import rider,driver,ride
from faker import Faker

fakegen = Faker()
# topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=8):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        # top = add_topic()
        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        # Create new rider Entry
        Rider = rider.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]

        # Create new driver Entry
        Driver = driver.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]

        # Create new ride Entry
        Ride = ride.objects.get_or_create(first_name=Rider,
                                        url=fake_url,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
