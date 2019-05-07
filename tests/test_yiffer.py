import unittest
from derp import Yiffer


class TestYiffer(unittest.TestCase):

    def setUp(self):
        self.yiffer = Yiffer()

    def test__dummy(self):
        self.assertTrue(True)
    
    def test__yiff_me__name(self):
        msg = self.yiffer.yiff_me('democelot')
        self.assertEqual(msg, 'I like to yiff democelot UwU')