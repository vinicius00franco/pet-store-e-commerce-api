from django.urls import path
from .views import UserRegistrationView, CustomAuthToken, LogoutView

urlpatterns = [
    path("signup/", UserRegistrationView.as_view(), name="signup"),
    path("login/", CustomAuthToken.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
