from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserAuthenticationForm, CustomUserCreationForm, ProfileForm
from .models import CustomUser

# Create your views here.

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  template_name = "registration/signup.html"
  success_url = reverse_lazy("login")

  def form_valid(self, form):
    response = super().form_valid(form)
    messages.success(
        self.request,
        "Account created successfully! You can now log in.",
    )
    return response


class CustomLoginView(LoginView):
  authentication_form = CustomUserAuthenticationForm
  template_name = "registration/login.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
  model = CustomUser
  form_class = ProfileForm
  template_name = "accounts/profile.html"
  success_url = reverse_lazy("profile")

  def get_object(self, queryset=None):
    # Users can only edit their own profile.
    return self.request.user

  def form_valid(self, form):
    messages.success(self.request, "Your profile has been updated.")
    return super().form_valid(form)
