import unittest

from s4.models.s4.s4d import S4D

class TestS4(unittest.TestCase):
    def test_init(self):

        _ = S4D(
            d_model=128,
            lr=None
        )