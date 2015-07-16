#!/bin/env python3
import requests
from django.test import TestCase
import json

class CRUDTestCase(TestCase):

    endpoint = "http://localhost:8080/"
    u = ""
    p = ""

    def setUp(self):
        print("CRUD setUp")
    
    def test_hello_world(self):
        print("Hello World")
        self.assertEqual(1+1, 2)
    
    # def test_create(self):
        # path = "/"
        # r = requests.get(self.ENDPOINT + path)
        # print(r.status_code)
        # self.assertEqual(r.status_code, 200)
    
    def test_read(self):
        # Create building, add to DB
        
        # Retrieve created building
        path = "get/building"
        r = requests.get(self.endpoint + path); #, auth=(self.u, self.p))
        
        # Run tests
        self.assertContains(r, "", status_code=200)
        self.assertJSONEqual(r.json(), '{"name": "USGBC", "address":"2101 L Street", "leed_id": 1000000117, "certification": "platinum"}')

    # def test_update(self):
        # path = "/"
        # r = requests.get(self.ENDPOINT + path)
        # print(r.status_code)
        # self.assertEqual(r.status_code, 200)

    # def test_delete(self):
        # path = "/"
        # r = requests.get(self.ENDPOINT + path)
        # print(r.status_code)
        # self.assertEqual(r.status_code, 200)
