from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.UserCreateView.as_view(), name='sign-up'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('email-verify', views.EmailVerificationView.as_view(), name='email-verify'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('active-profiles-list/', views.ActiveProfileListView.as_view(), name='active-profiles-list')


]