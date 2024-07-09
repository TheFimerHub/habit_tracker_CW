from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ObtainTokenPairView

app_name = 'users'

router = DefaultRouter()
router.register(r'register', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
]
