#!/bin/env python3
import requests
from django.test import TestCase

class CRUDTestCase(TestCase):

    ENDPOINT = "https://www.leedon.io"
    u = ""
    p = ""

    def setUp(self):
        print("CRUD setUp")
    
    def test_init(self):
        self.assertEqual(1+1, 2)
    
    # def test_create(self):
        # path = "/"
        # r = requests.get(self.ENDPOINT + path)
        # print(r.status_code)
        # self.assertEqual(r.status_code, 200)
    
    def test_read(self):
        path = ""
        r = requests.get(self.ENDPOINT + path);#, auth=(self.u, self.p))
        print(r.status_code)
        self.assertEqual(r.status_code, 200)

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
