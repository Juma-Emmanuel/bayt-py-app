from django.contrib import admin
from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
app_name = "baytApp"
urlpatterns = [
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth-refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('user-register/', UserRegistrationView.as_view(), name='cust-registration-api'),
    path('users/', UsersView.as_view(), name='users-list'),
    path('create-job/', CreateJobView.as_view(), name='create-job'),
    path('update-job/<int:pk>/', UpdateJobView.as_view(), name='update-job'),
    path('delete-job/<int:pk>/', DeleteJobView.as_view(), name='delete-job'),
    path('premium-jobs/', PremiumJobView.as_view(), name='jobs'),
    path('jobs/', JobView.as_view(), name='jobs'),

]