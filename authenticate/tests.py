from django.test import TestCase
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


class AuthenticateViewTest(TestCase):
    """Class to test authenticate views"""

    def test_register_user(self):
        # Test registering the user
        response = self.client.get(reverse("register"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submit")

    def test_login(self):
        # Test the login view
        user = User.objects.create(username="testuser")
        user.set_password("1234")
        user.save()

        response = self.client.post(
            reverse("login"),
            {"username": "testuser", "password": "1234"},
            follow=True,
        )

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("_auth_user_id", self.client.session)

    def test_logout(self):
        # Test the logout view
        # Create a user
        user = User.objects.create(username="testuser")
        user.set_password("1234")
        user.save()

        # Login the user
        self.client.login(username="testuser", password="1234")

        # Logout the user
        response = self.client.get(reverse("logout"), follow=True)
        user = auth.get_user(self.client)

        # Assert that user is not logged in
        self.assertFalse(user.is_authenticated)
        self.assertEqual(response.status_code, 200)
