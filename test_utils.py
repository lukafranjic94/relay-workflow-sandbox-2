import unittest

from utils import slugify


class SlugifyTests(unittest.TestCase):
    def test_example_phrase(self):
        self.assertEqual(slugify("Hello, Relay World!"), "hello-relay-world")

    def test_empty_input(self):
        self.assertEqual(slugify(""), "")

    def test_repeated_separators(self):
        self.assertEqual(slugify("foo---bar"), "foo-bar")
        self.assertEqual(slugify("a   b"), "a-b")


if __name__ == "__main__":
    unittest.main()
