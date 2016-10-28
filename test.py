import unittest
from dehash import dehash


class TestFactorial(unittest.TestCase):
    """
    Basic test for the dehash function
    """

    def test_dehash_developer(self):
        """
        Test for the developer entry.
        """
        res = dehash(956446786872726)
        self.assertEqual(res, "trellises")

    def test_dehash_android(self):
        """
        Test for the android developer entry.
        """
        res = dehash(25180466553932)
        self.assertEqual(res, "lollipop")


if __name__ == '__main__':
    unittest.main()
