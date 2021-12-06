import datetime

from django.test import TestCase
from django.utils import timezone

from forms import UniversityForm

# Following this tutorial for test cases
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

class TestFormUniversity(TestCase):

    def test_country_label(self):
        form = UniversityForm()
        self.assertTrue(form.fields['country'].label is None or form.fields['country'].label == 'country')

    def test_university_name_label(self):
        form = UniversityForm()
        self.assertTrue(form.fields['university_name'].label is None or form.fields['country'].label == 'university name')
