
from django.urls import path
from .views import UserRegistrationAPIView, UserProfileAPIView, UserLoginAPIView,MyTokenObtainPairView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('profile/<str:username>/', UserProfileAPIView.as_view(), name='user-profile'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
