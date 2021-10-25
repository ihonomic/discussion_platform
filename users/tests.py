from rest_framework.test import APITestCase


class TestAuth(APITestCase):
    '''
        Testing the auth process 
    '''
    login_url = '/profile/signin'
    register_url = '/profile/signup'

    def test_register(self):
        payload = {
            "username": "ihon",
            "email": "a@gmail.com",
            "password": "12345",
        }
        #   Make the request
        response = self.client.post(self.register_url, data=payload)
        result = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(result["details"])

    def test_login(self):
        payload = {
            "username": "ihon",
            "email": "a@gmail.com",
            "password": "12345",
        }
        #   register first
        self.client.post(self.register_url, data=payload)
        #   Login next
        response = self.client.post(self.login_url, data=payload)
        self.assertEqual(response.status_code, 200)
        #   check if tokens were generated
        result = response.json()
        self.assertEqual(result["username"], 'ihon')
