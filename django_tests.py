REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissions'
	]
}

from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from accounts.models import User 
from .factories import StaffUserFactory 

class MainSetUp(TestCase):
	def setUp(self): 
		self.user = StaffUserFactory
		self.api_root = '/api/v0'
		self.client = APIClient()

class APITests(MainSetUp, APITestCase):
	def test_create_feedback(self): 
		self.client.login(username='staffuser', password='password')

		url = '%sfeedback/' % self.api_root
		data = {
			'feedback': 'test feedback'
		}
		response = self.client.post(url, data, user=self.user)

		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.data, data)