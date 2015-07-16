import requests
from django.test import TestCase

class CRUDBuildingTestCase(TestCase):

    ENDPOINT = "https://www.leedon.io"

    def setUp(self):
        print "CRUD setUp"
	print "ENDPOINT = " + self.ENDPOINT
    
    def test_init(self):
        self.assertEqual(1+1, 2)
    
    # def test_create(self):
        # path = "/"
        # r = requests.get(self.ENDPOINT + path)
        # print r.status_code
        # print r.body
        # self.assertEqual(r.status_code, 200)
    
    def test_read(self):
        path = "/"
        r = requests.get(self.ENDPOINT + path)
        print r.status_code
        print r.body
        self.assertEqual(r.status_code, 200)

    # def test_update(self):
        # path = "/"
        # r = requests.get(self.ENDPOINT + path)
        # print r.status_code
        # print r.body
        # self.assertEqual(r.status_code, 200)

    # def test_delete(self):
        # path = "/"
        # r = requests.get(self.ENDPOINT + path)
        # print r.status_code
        # print r.body
        # self.assertEqual(r.status_code, 200)
