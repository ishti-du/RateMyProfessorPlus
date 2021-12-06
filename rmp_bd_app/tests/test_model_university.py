from django.test import TestCase

from models import Country, University

# Following this tutorial for test cases
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

class TestModelUniversity(TestCase):

    # Sets up objects that aren't modified or changed in any of the test methods
    def setUpTestData(cls):
        University.objects.create(country="United States of America", university_name="Test University")
    
    # Sets up objects that may be modified by the test (Every test gets a fresh version of these objects)
    def setUp(self):
        pass

    def test_country_label(self):
        university = University.objects.get(id=1)
        field_label = university._meta.get_field('country').verbose_name
        self.assertEqual(field_label, 'country')

    def test_university_name_label(self):
        university = University.objects.get(id=1)
        field_label = university._meta.get_field('university_name').verbose_name
        self.assertEqual(field_label, 'university name')

    def test_get_absolute_url(self):
        university = University.objects.get(id=1)
        self.assertEqual(university.get_absolute_url(), '/university/1/Campus')