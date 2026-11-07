from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class SignUpFeedbackTests(TestCase):
    def test_success_message_shown_after_signup(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "carol",
                "email": "carol@example.com",
                "first_name": "Carol",
                "last_name": "",
                "course": "BSIT",
                "password1": "V3ry-strong-pass!",
                "password2": "V3ry-strong-pass!",
            },
            follow=True,
        )
        self.assertRedirects(response, reverse("login"))
        self.assertTrue(CustomUser.objects.filter(username="carol").exists())
        self.assertContains(response, "Account created successfully")

    def test_base_template_loads_bootstrap(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "bootstrap@5.3.3/dist/css/bootstrap.min.css")
        self.assertContains(response, "form-control")


class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="alice", password="s3cret-pass-123", course="BSIT"
        )
        self.other = CustomUser.objects.create_user(
            username="bob", password="s3cret-pass-123"
        )

    def test_profile_requires_login(self):
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])

    def test_profile_page_renders_for_logged_in_user(self):
        self.client.login(username="alice", password="s3cret-pass-123")
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")
        self.assertContains(response, "alice")

    def test_user_can_update_own_profile(self):
        self.client.login(username="alice", password="s3cret-pass-123")
        response = self.client.post(
            reverse("profile"),
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "email": "alice@example.com",
                "course": "BSCS",
            },
        )
        self.assertRedirects(response, reverse("profile"))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Alice")
        self.assertEqual(self.user.last_name, "Smith")
        self.assertEqual(self.user.email, "alice@example.com")
        self.assertEqual(self.user.course, "BSCS")

    def test_profile_form_cannot_change_username_or_role(self):
        self.client.login(username="alice", password="s3cret-pass-123")
        self.client.post(
            reverse("profile"),
            {
                "first_name": "",
                "last_name": "",
                "email": "",
                "course": "",
                "username": "hacker",
                "role": CustomUser.Role.ADMIN,
            },
        )
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "alice")
        self.assertEqual(self.user.role, CustomUser.Role.STUDENT)

    def test_profile_update_does_not_touch_other_users(self):
        self.client.login(username="alice", password="s3cret-pass-123")
        self.client.post(
            reverse("profile"),
            {"first_name": "Changed", "last_name": "", "email": "", "course": ""},
        )
        self.other.refresh_from_db()
        self.assertEqual(self.other.first_name, "")
