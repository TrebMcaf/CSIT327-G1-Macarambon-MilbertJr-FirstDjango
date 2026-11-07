from django.urls import path
from .views import CustomLoginView, SignUpView, ProfileUpdateView

urlpatterns = [
  path("signup/", SignUpView.as_view(), name="signup"),
  path("profile/", ProfileUpdateView.as_view(), name="profile"),
  # Overrides the built-in login from django.contrib.auth.urls (listed later).
  path("login/", CustomLoginView.as_view(), name="login"),
]
