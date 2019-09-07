from django.test import TestCase
from .models import Broseph, Item
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class BrosephModelTests(TestCase):
# Create your tests here.
    def test_callAccurateInformationFromBrosephPostCreation(self):
        broseph = Broseph()
        anyUser = User(username="anyUser")
        anyUser.save()
        anyName = 'anyName'
        anyAttendanceDetails = 'I will be arriving when I arrive!'
        broseph.user = anyUser
        broseph.name = anyName
        broseph.attendance_details = anyAttendanceDetails
        broseph.save()

        self.assertEquals(broseph.name,anyName)

class ItemModelTests(TestCase):
    # Create your tests here.
    def test_callAccurateInformationFromItemPostCreation(self):
        itemName = "Nintendo Switch"
        item = Item()
        item.name = itemName
        item.save()

        self.assertEquals(item.name,itemName)
