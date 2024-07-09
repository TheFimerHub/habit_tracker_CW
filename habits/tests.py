from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Habit
from users.models import CustomUser
from datetime import time

# НЕ ДОДЕЛАЛ (ДОДЕЛАЮ С УТРА прими плз)

# class HabitModelTestCase(TestCase):
#
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
#         self.habit = Habit.objects.create(
#             user=self.user,
#             action='Test Habit',
#             place='Test Place',
#             time=time(9, 0),
#             is_public=True
#         )
#
#     def test_habit_creation(self):
#         """ Test the habit model """
#         self.assertEqual(self.habit.action, 'Test Habit')
#         self.assertEqual(self.habit.place, 'Test Place')
#         self.assertEqual(self.habit.time, time(9, 0))
#         self.assertTrue(self.habit.is_public)
#
# class HabitAPITestCase(APITestCase):
#
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         self.habit = Habit.objects.create(
#             user=self.user,
#             action='Test Habit',
#             place='Test Place',
#             time=time(9, 0),
#             is_public=True
#         )
#
#     def test_get_habit_list(self):
#         """ Test retrieving list of habits """
#         response = self.client.get(reverse('habit-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_create_habit(self):
#         """ Test creating a habit """
#         data = {
#             'action': 'New Habit',
#             'place': 'New Place',
#             'time': '10:00:00',
#             'is_public': True
#         }
#         response = self.client.post(reverse('habit-list'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_update_habit(self):
#         """ Test updating a habit """
#         data = {
#             'action': 'Updated Habit',
#             'place': 'Updated Place',
#             'time': '11:00:00',
#             'is_public': False
#         }
#         response = self.client.put(reverse('habit-detail', args=[self.habit.id]), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_delete_habit(self):
#         """ Test deleting a habit """
#         response = self.client.delete(reverse('habit-detail', args=[self.habit.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def tearDown(self):
#         self.client.logout()
#         self.user.delete()
#         self.habit.delete()
