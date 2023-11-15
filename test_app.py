import unittest
from app import create_app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_wisdom_endpoint(self):
        response = self.client.get('/wisdom')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Content-Type', response.headers)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_random_wisdom_endpoint(self):
        response = self.client.get('/wisdom/random')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Content-Type', response.headers)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertTrue(response.json)

if __name__ == '__main__':
    unittest.main()
