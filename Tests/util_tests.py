import unittest
import util


class MyTestCase(unittest.TestCase):

    # tests util.contains_token
    def test_contains_token(self):
        self.assertTrue(util.contains_token("a b c", "a"))
        self.assertTrue(util.contains_token("a b c", "b"))
        self.assertTrue(util.contains_token("a b c", "c"))
        self.assertFalse(util.contains_token("abc", "b"))

        self.assertFalse(util.contains_token("serial", "se"))
        self.assertTrue(util.contains_token("go se", "se"))


if __name__ == '__main__':
    unittest.main()
