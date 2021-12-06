from django.test import TestCase
from django.urls import reverse

from models import University

# Following this tutorial for test cases
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

class TestViewUniversity(TestCase):

    # Create 5 dummy universities
    def setUpTestData(cls):
        number_of_universities = 5

        for univ_id in range(number_of_universities):
            University.objects.create(
                country= 'United States of America',
                university_name = f'Test University {univ_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/university/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('university'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('university'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/university/')

    def test_pagination(self):
        response = self.client.get(reverse('university'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['university_list']), 5)