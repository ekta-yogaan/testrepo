import requests
from django.test import TestCase

class CRUDBuildingTestCase(TestCase):
    def setUp(self):
        print "CRUD setUp"
    
    def test_init(self):
        self.assertEqual(1+1, 2)
    
    def test_read(self):
        auth = "https://www.leedon.io"
        path = "/"
        r = requests.get(auth + path)
        print r.status_code
        print r.body
        self.assertEqual(r.status_code, 200)
