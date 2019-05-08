import unittest
import json
from derp import Yiffer
from app import app


class TestRoutesYiff(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.yiffer = Yiffer()

    def test__get_yiff__success(self):
        res = self.app.get('/yiff')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(200, res.status_code)
        self.assertEqual(200, data['code'])
        self.assertEqual("Yiff me daddy", data['message'])
    
    def test__yiff_me__name(self):
        msg = self.yiffer.yiff_me('democelot')
        self.assertEqual(msg, 'I like to yiff democelot UwU')