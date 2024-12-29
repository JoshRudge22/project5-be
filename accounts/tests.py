from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Follow

class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

    def test_follow_creation(self):
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.followed, self.user2)
        self.assertEqual(Follow.objects.count(), 1)

    def test_str_representation(self):
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertEqual(str(follow), "user1 follows user2")


class FollowViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

    def test_follow_user(self):
        self.client.login(username='user1', password='password1')
        url = reverse('follow-user')
        response = self.client.post(url, {'followed': self.user2.username})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Follow.objects.count(), 1) 

    def test_unfollow_user(self):
        Follow.objects.create(follower=self.user1, followed=self.user2)
        self.client.login(username='user1', password='password1')
        url = reverse('unfollow-user', args=[self.user2.username])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Follow.objects.count(), 0)

    def test_list_followers(self):
        Follow.objects.create(follower=self.user2, followed=self.user1)
        url = reverse('list-followers', args=[self.user1.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user2', [f['follower'] for f in response.json()])

    def test_list_following(self):
        Follow.objects.create(follower=self.user1, followed=self.user2)
        url = reverse('list-following', args=[self.user1.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user2', [f['followed'] for f in response.json()])