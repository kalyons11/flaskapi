import unittest

from flaskapi import app


class APITest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_another(self):
        self.assertTrue(True)
