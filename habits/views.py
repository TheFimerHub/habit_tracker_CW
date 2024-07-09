# views.py
from rest_framework import viewsets, permissions, generics
from django.core.exceptions import PermissionDenied
from .models import Habit
from .paginator import CustomPageNumberPagination
from .serializers import HabitSerializer
from .tasks import send_telegram_message

class HabitViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user, is_public=True)

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)
        text = f"Новая привычка создана: {habit.action} в {habit.place} в {habit.time}"
        send_telegram_message.delay(self.request.user.telegram_chat_id, text)

    def perform_update(self, serializer):
        habit = serializer.save()
        text = f"Привычка обновлена: {habit.action} в {habit.place} в {habit.time}"
        send_telegram_message.delay(self.request.user.telegram_chat_id, text)

    def perform_destroy(self, instance):
        text = f"Привычка удалена: {instance.action} в {instance.place} в {instance.time}"
        send_telegram_message.delay(self.request.user.telegram_chat_id, text)
        instance.delete()

class PublicHabitViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = CustomPageNumberPagination
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [permissions.AllowAny]

class UserHabitsListView(generics.ListAPIView):
    pagination_class = CustomPageNumberPagination
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)
