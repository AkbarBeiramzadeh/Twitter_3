from accounts.models import User
from django.test import TestCase
from .models import Post


class PostModelTestCase(TestCase):
    """

    """
    def setUp(self):
        """

        :return:
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )
        self.post = Post.objects.create(
            user=self.user,
            title='Test Post',
            text='This is a test post.',
        )

    def test_user_can_like(self):
        """

        :return:
        """
        self.assertFalse(self.post.user_can_like(self.user))
        self.post.likes.create(user=self.user)
        self.assertTrue(self.post.user_can_like(self.user))


