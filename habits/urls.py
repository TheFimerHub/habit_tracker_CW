from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, PublicHabitViewSet, UserHabitsListView

app_name = 'habit'

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'public-habits', PublicHabitViewSet, basename='public-habit')

urlpatterns = [
    path('', include(router.urls)),
    path('user/habits/', UserHabitsListView.as_view(), name='user-habits-list'),
]
