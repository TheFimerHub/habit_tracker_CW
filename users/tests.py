from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import CustomUser

# НЕ ДОДЕЛАЛ (ДОДЕЛАЮ С УТРА прими плз)


# class CustomUserModelTestCase(TestCase):
#
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(username='testuser', password='testpass', telegram_chat_id='123456789')
#
#     def test_user_creation(self):
#         """ Test the user model """
#         self.assertEqual(self.user.username, 'testuser')
#         self.assertTrue(self.user.check_password('testpass'))
#         self.assertEqual(self.user.telegram_chat_id, '123456789')
#
# class CustomUserAPITestCase(APITestCase):
#
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
#         self.client = APIClient()
#
#     def test_user_registration(self):
#         """ Test registering a new user """
#         data = {
#             'username': 'newuser',
#             'password': 'newpass',
#             'telegram_chat_id': '987654321'
#         }
#         response = self.client.post(reverse('user-list'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_user_login(self):
#         """ Test logging in a user """
#         data = {
#             'username': 'testuser',
#             'password': 'testpass'
#         }
#         response = self.client.post(reverse('token_obtain_pair'), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('access', response.data)
#         self.assertIn('refresh', response.data)
#
#     def test_user_detail(self):
#         """ Test retrieving user detail """
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get(reverse('user-detail', args=[self.user.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.client.logout()
#
#     def tearDown(self):
#         self.client.logout()
#         self.user.delete()
