import unittest
import requests
from index import *


 
class BasicTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_FORWARDED_FOR_header(self):
        fakeIP = '1.1.1.1'

        client = app.test_client()
        response = client.get('/', environ_base={'HTTP_X_FORWARDED_FOR': fakeIP})       
        assert fakeIP in response.data
    
    def test_REMOTE_ADDR_header(self):
        fakeIP = '1.1.1.222'

        client = app.test_client()
        response = client.get('/', environ_base={'REMOTE_ADDR': fakeIP})       
        assert fakeIP in response.data
    
    def test_REMOTE_IP(self):
        remoteIP = requests.get('http://ip.42.pl/raw').text

        client = app.test_client()
        response = client.get('/')
        assert remoteIP in response.data
 
 
if __name__ == "__main__":
    unittest.main()