from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from .models import StickyNote


class StickyNoteModelTest(TestCase):
    """Class to test Sticky Note Model objects."""

    def setUp(self):
        # Create a Sticky Note object
        StickyNote.objects.create(
            title="TestNote",
            content="This is a test",
            author="Author",
        )

    def test_sticky_note_title(self):
        # Test that a sticky note has the expected title
        sticky_note = StickyNote.objects.get(id=1)

        # Assert
        self.assertEqual(sticky_note.title, "TestNote")

    def test_sticky_note_content(self):
        # Test that a sticky note has the expected content
        sticky_note = StickyNote.objects.get(id=1)

        # Assert
        self.assertEqual(sticky_note.content, "This is a test")

    def test_sticky_note_author(self):
        # Test that a sticky note has the expected author
        sticky_note = StickyNote.objects.get(id=1)

        # Assert
        self.assertEqual(sticky_note.author, "Author")


class StickyNoteViewTest(TestCase):
    """Class to test Sticky Note views"""

    def setUp(self):
        # Create a user and give it the permissions
        change_permission = Permission.objects.get(
            codename="change_stickynote",
        )

        add_permission = Permission.objects.get(
            codename="add_stickynote",
        )

        user = User.objects.create(username="testuser")
        user.set_password("1234")
        user.user_permissions.add(change_permission)
        user.user_permissions.add(add_permission)
        user.save()

        # Login the user
        self.client.login(username="testuser", password="1234")

        # Create a Sticky Note object
        StickyNote.objects.create(
            title="TestNote",
            content="This is a test",
            author="Author",
        )

    def test_sticky_note_list_view(self):
        # Test the sticky notes list
        response = self.client.get(reverse("note_list"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestNote")

    def test_sticky_note_detail(self):
        # Test the sticky note detail

        response = self.client.get(reverse("note_detail", args=["1"]))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestNote")
        self.assertContains(response, "This is a test")

    def test_sticky_note_update_get(self):
        # Test the sticky note update showing the form
        response = self.client.get(reverse("note_update", args=["1"]))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title")
        self.assertContains(response, "Content")
        self.assertContains(response, "Author")
        self.assertContains(response, "Save")

    def test_sticky_note_update_post(self):
        # Test the sticky note update, updates the note
        response = self.client.post(
            reverse("note_update", args=["1"]),
            {
                "title": "New Title",
                "content": "New Content",
                "author": "New Author",
            },
            follow=True,
        )

        # Assert
        self.assertEqual(response.status_code, 200)
        sticky_note = StickyNote.objects.get(id=1)
        self.assertEqual(sticky_note.title, "New Title")
        self.assertEqual(sticky_note.content, "New Content")
        self.assertEqual(sticky_note.author, "New Author")

    def test_sticky_note_create_get(self):
        # Test the sticky note create
        response = self.client.get(reverse("note_create"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title")
        self.assertContains(response, "Content")
        self.assertContains(response, "Author")
        self.assertContains(response, "Save")

    def test_sticky_note_delete(self):
        # Test the sticky note delete
        response = self.client.delete(
            reverse("note_delete", args=["1"]),
            follow=True,
        )

        # Assert
        self.assertEqual(response.status_code, 200)

        # Assert that the sticky note does not exists anymore
        sticky_note_exists = StickyNote.objects.filter(id=1).exists()
        self.assertFalse(sticky_note_exists)
