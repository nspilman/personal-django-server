# from django.contrib.auth.models import User
from faker import Faker
fake = Faker()

def fakeuser():
    username = (fake.name().replace(" ","").lower())
    email = fake.email()
    password = "rockon"
    return {'username':username,'email':email,'password':password}

def fakeaddress():
    return fake.address()