from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import views


urlpatterns = [
    path('user/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
]
