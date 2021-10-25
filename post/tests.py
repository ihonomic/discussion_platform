from rest_framework.test import APITestCase


class TestPost(APITestCase):
    '''
        Testing the auth process 
    '''
    home_url = '/'
    like_url = '/like/1'

    def setUp(self):
        from django.contrib.auth.models import User

        #   first user
        self.user1 = User.objects.create(
            username="ihon", password="12345", email="e@gmail.com")

        #   second user
        self.user2 = User.objects.create_user(
            username="John", password="123456", email="eh@gmail.com")

        #   Authenticate client
        self.client.force_authenticate(user=self.user1)

    def test_create_post(self):
        payload = {
            "title": "First Title by Ihon",
            "post_content": "First Content"
        }
        #   Make the request
        response = self.client.post(self.home_url, data=payload)
        result = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(result["title"])
