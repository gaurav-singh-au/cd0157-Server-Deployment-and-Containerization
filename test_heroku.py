# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:26:17 2021

@author: gsing
"""


import requests
import unittest

URL ='https://fsnd-kubernetes.herokuapp.com/'

EMAIL = 'abc@xyz.com'
PWD = 'mypwd'
HEADERS = {'Content-Type': 'application/json'}

class herokuTestCase(unittest.TestCase):
    def testGetToken(self):
        res = requests.post(URL+"auth",headers=HEADERS,json={"email":EMAIL,
                                                             "password":PWD})
        TOKEN = res.json()['token']

        HEADERS2 = {"Authorization": "Bearer %s"%TOKEN}
        res2 = requests.get(URL+"contents", headers = HEADERS2)

        self.assertEqual(res2.json()['email'],EMAIL)
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
